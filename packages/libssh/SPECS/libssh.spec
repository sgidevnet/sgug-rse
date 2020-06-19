Name:           libssh
Version:        0.9.4
Release:        2%{?dist}
Summary:        A library implementing the SSH protocol
License:        LGPLv2+
URL:            http://www.libssh.org

Source0:        https://www.libssh.org/files/0.9/%{name}-%{version}.tar.xz
Source1:        https://www.libssh.org/files/0.9/%{name}-%{version}.tar.xz.asc
Source2:        https://cryptomilk.org/gpgkey-8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D.gpg#/%{name}.keyring
Source3:        libssh_client.config
Source4:        libssh_server.config

Patch0:         libssh-0.9.4-enable-sshd-sha1-algorithms.patch
Patch1:         libssh-0.9.4-fix-version.patch

Patch100:       libssh.sgifixes.patch

BuildRequires:  cmake >= 3.17.2-6
BuildRequires:  gcc-c++
#BuildRequires:  gnupg2
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
#BuildRequires:  krb5-devel
BuildRequires:  libcmocka-devel
#BuildRequires:  pam_wrapper
#BuildRequires:  socket_wrapper
#BuildRequires:  nss_wrapper
#BuildRequires:  uid_wrapper
BuildRequires:  openssh-clients
BuildRequires:  openssh-server
BuildRequires:  nmap-ncat

Requires:       %{name}-config = %{version}-%{release}

Recommends:     crypto-policies

%ifarch aarch64 ppc64 ppc64le s390x x86_64
Provides: libssh_threads.so.4()(64bit)
%else
Provides: libssh_threads.so.4
%endif

%description
The ssh library was designed to be used by programmers needing a working SSH
implementation by the mean of a library. The complete control of the client is
made by the programmer. With libssh, you can remotely execute programs, transfer
files, use a secure and transparent tunnel for your remote programs. With its
Secure FTP implementation, you can play with remote files easily, without
third-party programs others than libcrypto (from openssl).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package config
Summary:        Configuration files for %{name}
BuildArch:      noarch
Obsoletes:      %{name} < 0.9.0-3

%description config
The %{name}-config package provides the default configuration files for %{name}.

%prep
#gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p1

# To generate patches
#exit 1

%build
if test ! -e "obj"; then
  mkdir obj
fi
export PREV_WD=`pwd`
cd obj
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
export CPPFLAGS="-D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS"

%cmake .. \
    -DUNIT_TESTING=OFF \
    -DCLIENT_TESTING=ON \
    -DSERVER_TESTING=ON \
    -DGLOBAL_CLIENT_CONFIG="%{_sysconfdir}/libssh/libssh_client.config" \
    -DGLOBAL_BIND_CONFIG="%{_sysconfdir}/libssh/libssh_server.config"

#    -DUNIT_TESTING=ON \
#    -DCLIENT_TESTING=ON \
#    -DSERVER_TESTING=ON \
#

%make_build VERBOSE=1

cd $PREV_WD

%install
make DESTDIR=%{buildroot} install/fast -C obj
install -d -m755 %{buildroot}%{_sysconfdir}/libssh
install -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/libssh/libssh_client.config
install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/libssh/libssh_server.config

#
# Workaround for the removal of libssh_threads.so
#
# This will allow libraries which link against libssh_threads.so or packages
# requiring it to continue working.
#
export PREV_WD=`pwd`
cd %{buildroot}%{_libdir}
for i in libssh.so*;
do
    _target="${i}"
    _link_name="${i%libssh*}libssh_threads${i##*libssh}"
    if [ -L "${i}" ]; then
        _target="$(readlink ${i})"
    fi
    ln -s "${_target}" "${_link_name}"
done;
cd $PREV_WD

#%%ldconfig_scriptlets

%check
export PREV_WD=`pwd`
cd obj
ctest --output-on-failure
cd $PREV_WD

%files
%doc AUTHORS BSD ChangeLog README
%license COPYING
%{_libdir}/libssh.so.4*
%{_libdir}/libssh_threads.so.4*

%files devel
%{_includedir}/libssh/
# own this to avoid dep on cmake -- rex
%dir  %{_libdir}/cmake/
%{_libdir}/cmake/libssh/
%{_libdir}/pkgconfig/libssh.pc
%{_libdir}/libssh.so
%{_libdir}/libssh_threads.so

%files config
%attr(0755,root,root) %dir %{_sysconfdir}/libssh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libssh/libssh_client.config
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libssh/libssh_server.config

%changelog
* Wed Apr 15 2020 Anderson Sasaki <ansasaki@redhat.com> - 0.9.4-2
- Added patch to fix returned version

* Thu Apr 09 2020 Anderson Sasaki <ansasaki@redhat.com> - 0.9.4-1
- Update to version 0.9.4
  https://www.libssh.org/2020/04/09/libssh-0-9-4-and-libssh-0-8-9-security-release/
- Removed inclusion of OpenSSH server configuration file from
  libssh_server.config
- Added patch to re-enable algorithms using sha1 in sshd for testing
- resolves: #1822529 - CVE-2020-1730

* Tue Dec 10 2019 Andreas Schneider <asn@redhat.com> - 0.9.3-1
- Update to version 0.9.3
- resolves: #1781780 - Fixes CVE-2019-14889

* Thu Nov 07 2019 Andreas Schneider <asn@redhat.com> - 0.9.2-1
- Upate to version 0.9.2
- resolves #1769370 - Remove the docs, they can be found on https://api.libssh.org/

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.9.0-5
- Add Obsoletes in libssh-config to avoid conflict with old libssh which
  installed the configuration files.

* Wed Jul 10 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.9.0-4
- Eliminate circular dependency with libssh-config subpackage

* Wed Jul 10 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.9.0-3
- Provide the configuration files in a separate libssh-config subpackage

* Thu Jul 04 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.9.0-2
- Do not ignore keys from known_hosts when SSH_OPTIONS_HOSTKEYS is set

* Fri Jun 28 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.9.0-1
- Fixed Release number to released format

* Fri Jun 28 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.9.0-0.1
- Update to version 0.9.0
  https://www.libssh.org/2019/06/28/libssh-0-9-0/

* Wed Jun 19 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.8.91-0.1
- Update to 0.9.0 pre release version (0.8.91)
- Added default configuration files for client and server
- Follow system-wide crypto configuration (crypto-policies)
- Added Recommends for crypto-policies
- Use OpenSSL implementation for KDF, DH, and signatures.
- Detect FIPS mode and use only allowed algorithms
- Run client and server tests during build

* Mon Feb 25 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.8.7-1
- Update to version 0.8.7
  https://www.libssh.org/2019/02/25/libssh-0-8-7/

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.8.6-2
- Fix rsa-sha2 extension handling (#1666342)

* Thu Jan 03 2019 Anderson Sasaki <ansasaki@redhat.com> - 0.8.6-1
- Update to version 0.8.6
  https://www.libssh.org/2018/12/24/libssh-0-8-6-xmas-edition/

* Mon Oct 29 2018 Andreas Schneider <asn@redhat.com> - 0.8.5-1
- Update to version 0.8.5
  https://www.libssh.org/2018/10/29/libssh-0-8-5-and-libssh-0-7-7/

* Tue Oct 16 2018 Andreas Schneider <asn@redhat.com> - 0.8.4-1
- Update to version 0.8.4
  https://www.libssh.org/2018/10/16/libssh-0-8-4-and-0-7-6-security-and-bugfix-release
- Fixes CVE-2018-10933

* Mon Oct 01 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.8.3-3
- Fixed errors found by static code analysis

* Tue Sep 25 2018 Anderson Sasaki <ansasaki@redhat.com> - 0.8.3-2
- Add missing libssh_threads.so link to libssh-devel package

* Fri Sep 21 2018 Andreas Schneider <asn@redhat.com> - 0.8.3-1
- Update to version 0.8.3
  https://www.libssh.org/2018/09/21/libssh-0-8-3/

* Thu Aug 30 2018 Andreas Schneider <asn@redhat.com> - 0.8.2-1
- Update to version 0.8.2
  https://www.libssh.org/2018/08/30/libssh-0-8-2

* Thu Aug 16 2018 Andreas Schneider <asn@redhat.com> - 0.8.1-4
- Fix link creation or RPM doesn't install it

* Wed Aug 15 2018 Andreas Schneider <asn@redhat.com> - 0.8.1-3
- Add missing so version for libssh_threads.so.4

* Tue Aug 14 2018 Andreas Schneider <asn@redhat.com> - 0.8.1-2
- Add Provides for libssh_threads.so to unbreak applications

* Mon Aug 13 2018 Andreas Schneider <asn@redhat.com> - 0.8.1-1
- Update to version 0.8.1
  https://www.libssh.org/2018/08/13/libssh-0-8-1
- resolves: #1615248 - pkg-config --modversion
- resolves: #1615132 - library initialization

* Fri Aug 10 2018 Andreas Schneider <asn@redhat.com> - 0.8.0-1
- Update to version 0.8.0
  https://www.libssh.org/2018/08/10/libssh-0-8-0/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.7.5-8
- BR: gcc-c++, use %%make_build

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Andreas Schneider <asn@redhat.com> - 0.7.5-6
- resolves: #1540021 - Build against OpenSSL 1.1

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.5-5
- Switch to %%ldconfig_scriptlets

* Fri Dec 29 2017 Andreas Schneider <asn@redhat.com> - 0.7.5-4
- Fix parsing ssh_config

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.5-1
- Update to version 0.7.5

* Sat Mar 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.7.4-2
- BR: compat-openssl10-devel (f26+, #1423088)
- use %%license
- -devel: drop hardcoded pkgconfig dep (let autodeps handle it)
- %%files: track library sonames, simplify -devel
- %%install: use 'install/fast' target
- .spec cosmetics, drop deprecated %%clean section

* Wed Feb 08 2017 Andreas Schneider <asn@redhat.com> - 0.7.4-1
- Update to version 0.7.4
  * Added id_ed25519 to the default identity list
  * Fixed sftp EOF packet handling
  * Fixed ssh_send_banner() to confirm with RFC 4253
  * Fixed some memory leaks
- resolves: #1419007

* Wed Feb 24 2016 Andreas Schneider <asn@redhat.com> - 0.7.3-1
- resolves: #1311259 - Fix CVE-2016-0739
- resolves: #1311332 - Update to version 0.7.3
  * Fixed CVE-2016-0739
  * Fixed ssh-agent on big endian
  * Fixed some documentation issues
- Enabled GSSAPI support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Andreas Schneider <asn@redhat.com> - 0.7.2-2
- resolves: #1271230 - Fix ssh-agent support on big endian

* Wed Sep 30 2015 Andreas Schneider <asn@redhat.com> - 0.7.2-1
- Update to version 0.7.2
  * Fixed OpenSSL detection on Windows
  * Fixed return status for ssh_userauth_agent()
  * Fixed KEX to prefer hmac-sha2-256
  * Fixed sftp packet handling
  * Fixed return values of ssh_key_is_(public|private)
  * Fixed bug in global success reply
- resolves: #1267346

* Tue Jun 30 2015 Andreas Schneider <asn@redhat.com> - 0.7.1-1
- Update to version 0.7.1
  * Fixed SSH_AUTH_PARTIAL auth with auto public key
  * Fixed memory leak in session options
  * Fixed allocation of ed25519 public keys
  * Fixed channel exit-status and exit-signal
  * Reintroduce ssh_forward_listen()

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-2
- Add patch to fix undefined symbol: ssh_forward_listen (bug #1221310)

* Mon May 11 2015 Andreas Schneider <asn@redhat.com> - 0.7.0-1
- Update to version 0.7.0
  * Added support for ed25519 keys
  * Added SHA2 algorithms for HMAC
  * Added improved and more secure buffer handling code
  * Added callback for auth_none_function
  * Added support for ECDSA private key signing
  * Added more tests
  * Fixed a lot of bugs
  * Improved API documentation

* Thu Apr 30 2015 Andreas Schneider <asn@redhat.com> - 0.6.5-1
- resolves: #1213775 - Security fix for CVE-2015-3146
- resolves: #1218076 - Security fix for CVE-2015-3146

* Fri Dec 19 2014 - Andreas Schneider <asn@redhat.com> - 0.6.4-1
- Security fix for CVE-2014-8132.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 - Andreas Schneider <asn@redhat.com> - 0.6.3-1
- Fix CVE-2014-0017.

* Mon Feb 10 2014 - Andreas Schneider <asn@redhat.com> - 0.6.1-1
- Update to version 0.6.1.
- resolves: #1056757 - Fix scp mode.
- resolves: #1053305 - Fix known_hosts heuristic.

* Wed Jan 08 2014 - Andreas Schneider <asn@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Fri Jul 26 2013 - Andreas Schneider <asn@redhat.com> - 0.5.5-1
- Update to 0.5.5.
- Clenup the spec file.

* Thu Jul 18 2013 Simone Caronni <negativo17@gmail.com> - 0.5.4-5
- Add EPEL 5 support.
- Add Debian patches to enable Doxygen documentation.

* Tue Jul 16 2013 Simone Caronni <negativo17@gmail.com> - 0.5.4-4
- Add patch for #982685.

* Mon Jun 10 2013 Simone Caronni <negativo17@gmail.com> - 0.5.4-3
- Clean up SPEC file and fix rpmlint complaints.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Petr Lautrbach <plautrba@redhat.com> 0.5.4-1
- update to security 0.5.4 release
- CVE-2013-0176 (#894407)

* Tue Nov 20 2012 Petr Lautrbach <plautrba@redhat.com> 0.5.3-1
- update to security 0.5.3 release (#878465)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Petr Lautrbach <plautrba@redhat.com> 0.5.2-1
- update to 0.5.2 version (#730270)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun  1 2011 Jan F. Chadima <jchadima@redhat.com> - 0.5.0-1
- bounce versionn to 0.5.0 (#709785)
- the support for protocol v1 is disabled

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Jan F. Chadima <jchadima@redhat.com> - 0.4.8-1
- bounce versionn to 0.4.8 (#670456)

* Mon Sep  6 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.6-1
- bounce versionn to 0.4.6 (#630602)

* Thu Jun  3 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.4-1
- bounce versionn to 0.4.4 (#598592)

* Wed May 19 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.3-1
- bounce versionn to 0.4.3 (#593288)

* Tue Mar 16 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.2-1
- bounce versionn to 0.4.2 (#573972)

* Tue Feb 16 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.1-1
- bounce versionn to 0.4.1 (#565870)

* Fri Dec 11 2009 Jan F. Chadima <jchadima@redhat.com> - 0.4.0-1
- bounce versionn to 0.4.0 (#541010)

* Thu Nov 26 2009 Jan F. Chadima <jchadima@redhat.com> - 0.3.92-2
- typo in spec file

* Thu Nov 26 2009 Jan F. Chadima <jchadima@redhat.com> - 0.3.92-1
- bounce versionn to 0.3.92 (0.4 beta2) (#541010)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.2-4
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Jan F. Chadima <jchadima@redhat.com> - 0.2-2
- Small changes during review

* Mon Jun 01 2009 Jan F. Chadima <jchadima@redhat.com> - 0.2-1
- Initial build

