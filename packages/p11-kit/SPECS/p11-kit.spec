# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

# This spec file has been automatically updated
Version:	0.23.16.1
Release:        6%{?dist}
Name:           p11-kit
Summary:        Library for loading and sharing PKCS#11 modules

License:        BSD
URL:            http://p11-glue.freedesktop.org/p11-kit.html
Source0:        https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.gz
Source1:        trust-extract-compat
Source2:        p11-kit-client.service

Patch100:       p11-kit.sgifixes.patch
Patch101:       p11-kit.sgifixpselect.patch

BuildRequires:  gcc
BuildRequires:  libtasn1-devel >= 2.3
BuildRequires:  libffi-devel >= 3.2.1-26
#BuildRequires:  gtk-doc
#BuildRequires:  systemd-devel
# Work around for https://bugzilla.redhat.com/show_bug.cgi?id=1497147
# Remove this once it is fixed
#BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libdicl-devel >= 0.1.19
Requires:       libdicl >= 0.1.19

%description
p11-kit provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

# Here's a terminator

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libdicl-devel >= 0.1.19

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package trust
Summary:            System trust module from %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           libdicl >= 0.1.19
Requires:           alternatives
Requires(post):     %{_sbindir}/update-alternatives
Requires(postun):   %{_sbindir}/update-alternatives
Conflicts:          nss < 3.14.3-9

%description trust
The %{name}-trust package contains a system trust PKCS#11 module which
contains certificate anchors and black lists.


#%%package server
#Summary:        Server and client commands for %%{name}
#Requires:       %%{name}%%{?_isa} = %%{version}-%%{release}

#%%description server
#The %%{name}-server package contains command line tools that enable to
#export PKCS#11 modules through a Unix domain socket.  Note that this
#feature is still experimental.


# solution taken from icedtea-web.spec
%define multilib_arches ppc64 sparc64 x86_64 ppc64le
%ifarch %{multilib_arches}
%define alt_ckbi  libnssckbi.so.%{_arch}
%else
%define alt_ckbi  libnssckbi.so
%endif


%prep
%autosetup -p1

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -DLIBDICL_NEED_GETOPT=1"
export LDFLAGS="-ldicl-0.1 -lgen -lpthread $RPM_LD_FLAGS"
# These paths are the source paths that  come from the plan here:
# https://fedoraproject.org/wiki/Features/SharedSystemCertificates:SubTasks
#configure --disable-static --enable-doc --with-trust-paths=%{_sysconfdir}/pki/ca-trust/source:%{_datadir}/pki/ca-trust-source --disable-silent-rules
%configure --disable-static --disable-doc --with-trust-paths=%{_sysconfdir}/pki/ca-trust/source:%{_datadir}/pki/ca-trust-source --disable-silent-rules --without-systemd
make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/modules
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/pkcs11/*.la
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_libexecdir}/p11-kit/
perl -pi -e "s|/usr/bin/bash|%{_bindir}/bash|g" $RPM_BUILD_ROOT%{_libexecdir}/p11-kit/trust-extract-compat
perl -pi -e "s|/usr/bin/update-ca-trust|%{_bindir}/update-ca-trust|g" $RPM_BUILD_ROOT%{_libexecdir}/p11-kit/trust-extract-compat

# Install the example conf with %%doc instead
rm $RPM_BUILD_ROOT%{_sysconfdir}/pkcs11/pkcs11.conf.example
#mkdir -p $RPM_BUILD_ROOT%{_userunitdir}
#install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_userunitdir}

# Remove unused server bits
rm $RPM_BUILD_ROOT%{_libdir}/pkcs11/p11-kit-client.so
rm $RPM_BUILD_ROOT%{_prefix}/libexec/p11-kit/p11-kit-server

%check
make check


%post trust
%{_sbindir}/update-alternatives --install %{_libdir}/libnssckbi.so \
        %{alt_ckbi} %{_libdir}/pkcs11/p11-kit-trust.so 30

%postun trust
if [ $1 -eq 0 ] ; then
        # package removal
        %{_sbindir}/update-alternatives --remove %{alt_ckbi} %{_libdir}/pkcs11/p11-kit-trust.so
fi


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README
%doc p11-kit/pkcs11.conf.example
%dir %{_sysconfdir}/pkcs11
%dir %{_sysconfdir}/pkcs11/modules
%dir %{_datadir}/p11-kit
%dir %{_datadir}/p11-kit/modules
%dir %{_libexecdir}/p11-kit
%{_bindir}/p11-kit
%{_libdir}/libp11-kit.so.*
%{_libdir}/p11-kit-proxy.so
%{_libexecdir}/p11-kit/p11-kit-remote
#%%{_mandir}/man1/trust.1.gz
#%%{_mandir}/man8/p11-kit.8.gz
#%%{_mandir}/man5/pkcs11.conf.5.gz

%files devel
%{_includedir}/p11-kit-1/
%{_libdir}/libp11-kit.so
%{_libdir}/pkgconfig/p11-kit-1.pc
%doc %{_datadir}/gtk-doc/

%files trust
%{_bindir}/trust
%dir %{_libdir}/pkcs11
%ghost %{_libdir}/libnssckbi.so
%{_libdir}/pkcs11/p11-kit-trust.so
%{_datadir}/p11-kit/modules/p11-kit-trust.module
%{_libexecdir}/p11-kit/trust-extract-compat

#%%files server
#%%{_libdir}/pkcs11/p11-kit-client.so
#%%{_userunitdir}/p11-kit-client.service
#%%{_libexecdir}/p11-kit/p11-kit-server
#%%{_userunitdir}/p11-kit-server.service
#%%{_userunitdir}/p11-kit-server.socket


%changelog
* Sat Nov 21 2020 Daniel Hams <daniel.hams@gmail.com> - 0.23.16.1-6
- Depend on bug-fixed libffi

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 0.23.16.1-5
- Fix incorrect dependency from p11-kit-trust on libdicl-devel

* Thu Feb 20 2020 Daniel Hams <daniel.hams@gmail.com> - 0.23.16.1-3
- Rebuild due to libdicl upgrade to 0.1.19

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Daiki Ueno <dueno@redhat.com> - 0.23.16.1-1
- Update to upstream 0.23.16.1 release

* Thu May 23 2019 Daiki Ueno <dueno@redhat.com> - 0.23.16-1
- Update to upstream 0.23.16 release

* Mon Feb 18 2019 Daiki Ueno <dueno@redhat.com> - 0.23.15-3
- trust: Ignore unreadable content in anchors

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
