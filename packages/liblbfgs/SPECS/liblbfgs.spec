Name:           liblbfgs
Version:        1.10
Release:        13%{?dist}
Summary:        Limited-memory Broyden-Fletcher-Goldfarb-Shanno library

License:        MIT
URL:            http://www.chokkan.org/software/liblbfgs/
Source0:        https://github.com/downloads/chokkan/liblbfgs/%{name}-%{version}.tar.gz
# Fix CFLAGS override, build solib with correct versioning
Patch0:         liblbfgs_build.patch

BuildRequires:  autoconf automake libtool

%description
A C port of the implementation of Limited-memory
Broyden-Fletcher-Goldfarb-Shanno (L-BFGS) method written by Jorge Nocedal.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1

# Needed for patch0
autoreconf -ifv


%build
export LDFLAGS="-Wl,--as-needed"
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Install these through %%doc
rm -rf %{buildroot}%{_datadir}/doc
rmdir %{buildroot}%{_datadir}


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/liblbfgs.so.*

%files devel
%{_includedir}/*
%{_libdir}/liblbfgs.so


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Sandro Mani <manisandro@gmail.com> - 1.10-3
- Add -Wl,--as-needed

* Fri Jun 20 2014 Sandro Mani <manisandro@gmail.com> - 1.10-2
- $RPM_BUILD_ROOT -> %%{buildroot}
- Add liblbfgs_build.patch

* Fri Jun 13 2014 Sandro Mani <manisandro@gmail.com> - 1.10-1
- Initial package
