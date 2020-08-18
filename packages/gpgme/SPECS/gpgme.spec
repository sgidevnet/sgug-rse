#%%global __strip /bin/true

%bcond_with check

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# STATUS_KEY_CONSIDERED has been added in 2.1.13
%global gnupg2_min_ver 2.1.13
%global libgpg_error_min_ver 1.24

Name:           gpgme
Summary:        GnuPG Made Easy - high level crypto API
Version:        1.13.1
Release:        7%{?dist}

License:        LGPLv2+
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source2:        gpgme-multilib.h

## downstream patches
# Don't add extra libs/cflags in gpgme-config/cmake equivalent
Patch1001:      0001-don-t-add-extra-libraries-for-linking.patch
# add -D_FILE_OFFSET_BITS... to gpgme-config, upstreamable
Patch1002:      gpgme-1.3.2-largefile.patch
# Let's fix stupid AX_PYTHON_DEVEL
Patch1003:      0001-fix-stupid-ax_python_devel.patch
# Make the make check work with gnupg-2.2.19 and above
Patch1004:      gpgme-build-with-gnupg-2.2.19.patch

Patch9000:      gpgme.sgifixes.patch

#BuildRequires:  autoconf
#BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gawk
BuildRequires:  gnupg2 >= %{gnupg2_min_ver}
BuildRequires:  gnupg2-smime
BuildRequires:  libgpg-error-devel >= %{libgpg_error_min_ver}
BuildRequires:  libassuan-devel >= 2.4.2

BuildRequires:  libdicl-devel >= 0.1.31

# For python bindings
BuildRequires:  swig

# to remove RPATH
#BuildRequires:  chrpath

# For AutoReq cmake-filesystem
BuildRequires:  cmake

Requires:       gnupg2 >= %{gnupg2_min_ver}

# On the following architectures workaround multiarch conflict of -devel packages:
%define multilib_arches %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libgpg-error-devel%{?_isa} >= %{libgpg_error_min_ver}

%description devel
%{summary}.

%package -n %{name}pp
Summary:        C++ bindings/wrapper for GPGME
Obsoletes:      gpgme-pp < 1.8.0-7
Provides:       gpgme-pp = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{name}pp
%{summary}.

%package -n %{name}pp-devel
Summary:        Development libraries and header files for %{name}-pp
Obsoletes:      gpgme-pp-devel < 1.8.0-7
Provides:       gpgme-pp-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-devel%{?_isa}
# For automatic provides
BuildRequires:  cmake

%description -n %{name}pp-devel
%{summary}

#%%package -n q%%{name}
#Summary:        Qt API bindings/wrapper for GPGME
#Requires:       %%{name}pp%%{?_isa} = %%{?epoch:%%{epoch}:}%%{version}-%%{release}
#BuildRequires:  pkgconfig(Qt5Core)
#BuildRequires:  pkgconfig(Qt5Test)
#
#%%description -n q%%{name}
#%%{summary}.

#%%package -n q%%{name}-devel
#Summary:        Development libraries and header files for %%{name}
## before libqgpgme.so symlink was moved to avoid conflict
#Conflicts:      kdepimlibs-devel < 4.14.10-17
#Requires:       q%%{name}%%{?_isa} = %%{?epoch:%%{epoch}:}%%{version}-%%{release}
#Requires:       %%{name}pp-devel%%{?_isa}
## For automatic provides
#BuildRequires:  cmake
#
#%%description -n q%%{name}-devel
#%%{summary}.

%package -n python3-gpg
Summary:        %{name} bindings for Python 3
%{?python_provide:%python_provide python3-gpg}
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      platform-python-gpg < %{version}-%{release}

%description -n python3-gpg
%{summary}.

%prep
%autosetup -p1

## HACK ALERT
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
#sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpgme-config.in

# The build machinery does not support Python 3.9+ yet
# https://github.com/gpg/gpgme/pull/4
sed -i 's/3.8/%{python3_version}/g' configure

# A place to generate the sgug patch
#exit 1

# Rewrite hardcoded /bin/sh paths in the tests
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/start-stop-agent
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/gpg/initial.test
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/gpg/final.test
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/gpg/pinentry.test
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/opassuan/t-command
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/gpgsm/initial.test
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/gpgsm/final.test
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/json/initial.test
perl -pi -e "s|/bin/sh|%{_bindir}/sh|g" tests/json/final.test

%build
# People neeed to learn that you can't run autogen.sh anymore
#./autogen.sh
# Use -I... directly because of https://bugzilla.redhat.com/show_bug.cgi?id=1742986
#CFLAGS="%{optflags} -I/usr/include/libassuan2"

export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
#CFLAGS="-g -O0 -I%{_includedir}/libassuan2"
#CXXFLAGS="-g -O0"
CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/libassuan2"
CXXFLAGS="$RPM_OPT_FLAGS"
#export LDFLAGS="-ldicl-0.1"
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"

#%%configure --disable-static --disable-silent-rules --enable-languages=cpp,qt,python
%configure --disable-static --disable-silent-rules --enable-languages=cpp,python
%make_build

%install
%make_install

# unpackaged files
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la

# Hack to resolve multiarch conflict (#341351)
#%ifarch %{multilib_arches}
#mv %{buildroot}%{_bindir}/gpgme-config{,.%{_target_cpu}}
#cat > gpgme-config-multilib.sh <<__END__
##!/bin/sh
#exec %{_bindir}/gpgme-config.\$(arch) \$@
#__END__
#install -D -p gpgme-config-multilib.sh %{buildroot}%{_bindir}/gpgme-config
#mv %{buildroot}%{_includedir}/gpgme.h \
#   %{buildroot}%{_includedir}/gpgme-%{__isa_bits}.h
#install -m644 -p -D %{SOURCE2} %{buildroot}%{_includedir}/gpgme.h
#%endif

#chrpath -d %{buildroot}%{_bindir}/%{name}-tool
#chrpath -d %{buildroot}%{_libdir}/lib%{name}pp.so*
#chrpath -d %{buildroot}%{_libdir}/libq%{name}.so*

# autofoo installs useless stuff for uninstall
rm -vf %{buildroot}%{python2_sitelib}/gpg/install_files.txt
rm -vf %{buildroot}%{python3_sitelib}/gpg/install_files.txt

# remove python2 pieces
rm -rf %{buildroot}%{python2_sitelib}

%if %{with check}
%check
make check
%endif

%files
%license COPYING*
%doc AUTHORS NEWS README*
%{_bindir}/%{name}-json
%{_libdir}/lib%{name}.so.11*

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-tool
#%ifarch %{multilib_arches}
#%{_bindir}/%{name}-config.%{_target_cpu}
#%{_includedir}/%{name}-%{__isa_bits}.h
#%endif
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_datadir}/aclocal/%{name}.m4
%{_infodir}/%{name}.info*
%{_libdir}/pkgconfig/%{name}*.pc

%files -n %{name}pp
%doc lang/cpp/README
%{_libdir}/lib%{name}pp.so.*

%files -n %{name}pp-devel
%{_includedir}/%{name}++/
%{_libdir}/lib%{name}pp.so
%{_libdir}/cmake/Gpgmepp/

#%%files -n q%%{name}
#%%doc lang/qt/README
#%%{_libdir}/libq%%{name}.so.*

#%%files -n q%%{name}-devel
#%%{_includedir}/q%%{name}/
#%%{_includedir}/QGpgME/
#%%{_libdir}/libq%%{name}.so
#%%{_libdir}/cmake/QGpgme/

%files -n python3-gpg
%doc lang/python/README
%{python3_sitearch}/gpg-*.egg-info
%{python3_sitearch}/gpg/

%changelog
* Thu Apr 30 2020 Tomáš Mráz <tmraz@redhat.com> - 1.13.1-7
- Fix FTBFS with gnupg-2.2.19 and above

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.13.1-4
- Rebuilt for Python 3.8

* Sat Aug 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.13.1-3
- Set real VERSION

* Sat Aug  3 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.13.1-2
- Move .pc files to devel so the base library doesn't pull in devel packages

* Mon Jul 29 18:46:42 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.13.1-1
- Update to 1.13.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-2
- Subpackage python2-gpg has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-2
- Rebuilt for Python 3.7

* Fri Apr 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Thu Apr 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Tue Apr 17 2018 Jonathan Lebon <jonathan@jlebon.com> - 1.10.0-4
- Backport patch to tweak STATUS_FAILURE handling

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.10.0-2
- Switch to %%ldconfig_scriptlets

* Wed Dec 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.0-8
- Use better Obsoletes for platform-python

* Fri Nov 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.0-7
- Remove platform-python subpackages

* Thu Aug 10 2017 Petr Viktorin <pviktori@redhat.com> - 1.9.0-6
- Add subpackage for platform-python (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Mon Aug 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.0-5
- Remove BuildRequires: pth-devel, it is not needed for long time

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 1.9.0-4
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Sat Feb 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.0-12
- Fix FTBFS

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.8.0-10
- patch out LIBASSUAN_LIBRARIES in cmake too

* Wed Jan 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.8.0-9
- gpgmepp-devel: Requires: libassuan-devel

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.8.0-8
- qgpgme-devel: Conflicts: kdepimlibs-devel < 4.14.10-17

* Sun Jan 01 2017 Rex Dieter <rdieter@math.unl.edu> - 1.8.0-7
- rename gpgme-pp to gpgmepp, simplify -devel deps

* Sun Jan 01 2017 Rex Dieter <rdieter@math.unl.edu> - 1.8.0-6
- backport upstream cmake-related fix

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-5
- Rebuild for Python 3.6

* Sun Dec 11 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.8.0-4
- Rename pythonX-gpgme into pythonX-gpg

* Sun Dec 11 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.8.0-3
- Add Qt and C++ subpackages

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.8.0-2
- Enable tests

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Wed Sep 21 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Mon Jul 25 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.6.0-3
- Set min ver for libgpg-error

* Mon Jul 25 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.6.0-2
- Backport patch for STATUS_KEY_CONSIDERED (RHBZ #1359521)

* Wed Jul 13 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.6.0-1
- Update to 1.6.0 (RHBZ #1167656)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 06 2014 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.4.3-5
- CVE-2014-3564, rhbz#1125170, gpgme-1.3.2-bufferoverflow.patch

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Tom Callaway <spot@fedoraproject.org> - 1.4.3-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 09 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.4.3-1
- gpgme-1.4.3
- cleanup .spec, trim changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Karsten Hopp <karsten@redhat.com> 1.3.2-3
- rebuild to fix some f20 dependency issues on PPC

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.3.2-2
- minor spec cleanup

* Wed Sep 26 2012 Tomas Mraz <tmraz@redhat.com> - 1.3.2-1
- new upstream version
- re-enable gpg tests (original patch by John Morris <john@zultron.com>)
- quiet configure warning 'could not find g13'
- there is no libgpgme-pth anymore

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-8
- -devel: make Requires: libgpg-error-devel arch'd
- ensure gpgme-config wrapper is executable

* Sun Apr 22 2012 Rex Dieter <rdieter@fedoraproject.org> 1.3.0-7
- gpgme.h: fatal error: gpgme-i386.h: No such file or directory compilation terminated (#815116)

* Wed Feb 15 2012 Simon Lukasik <slukasik@redhat.com> - 1.3.0-6
- Resolve multilib conflict of gpgme-config (#341351)
- Resolve multilib conflict of gpgme.h (#341351)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 17 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-4
- gpgme-config: remove libassuan-related flags as threatened (#676954) 
\
* Sun Feb 13 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-3
- -devel: fix typo (broken dep)

* Sat Feb 12 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-2
- BR: libassuan2-devel
- gpgme-config outputs -lassuan (#676954)

* Fri Feb 11 2011 Tomas Mraz <tmraz@redhat.com> - 1.3.0-1
- new upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 18 2010 Tomas Mraz <tmraz@redhat.com> - 1.2.0-3
- fix the condition for adding the -D_FILE_OFFSET_BITS...

* Wed Aug 11 2010 Tomas Mraz <tmraz@redhat.com> - 1.2.0-2
- add -D_FILE_OFFSET_BITS... to gpgme-config as appropriate (#621698)

* Fri Jul 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-1
- gpgme-1.2.0 (#610984)

* Sun Feb 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.8-4
- FTBFS gpgme-1.1.8-3.fc13: ImplicitDSOLinking (#564605)

* Thu Nov 19 2009 Tomas Mraz <tmraz@redhat.com> - 1.1.8-3
- Add buildrequires gnupg2-smime for the gpgsm

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.8-1
- gpgme-1.1.8
- -devel: s/postun/preun/ info scriptlet

* Wed Mar 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.7-3
- track shlib sonames closer, to highlight future abi/soname changes
- _with_gpg macro, to potentially conditionalize gnupg vs gnupg2 defaults
  for various os/releases (ie, fedora vs rhel)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.7-1
- gpgme-1.1.7

* Sun Feb 17 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.6-3
- --with-gpg=%%_bindir/gpg2 (#432445)
- drop Requires: gnupg (#432445)

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.6-2 
- respin (gcc43)

* Fri Jan 04 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.6-1
- gpgme-1.1.6
- multiarch conflicts in gpgme (#341351)

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.5-4
- BR: gawk

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.5-3
- respin (BuildID)

* Thu Aug 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.5-2
- License: LGPLv2+

* Mon Jul 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.5-1
- gpgme-1.1.5

* Mon Mar 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.4-1
- gpgme-1.1.4

* Sat Feb 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.3-1
- gpgme-1.1.3

* Tue Oct 03 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- respin

* Mon Sep 18 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-6
- fix gpgme-config --thread=pthread --cflags

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-5
- fc6 respin

* Mon Mar 6 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-4
- add back support for gpgme-config --thread=pthread

* Mon Mar 6 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-2
- drop extraneous libs from gpgme-config

* Fri Mar 3 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-1
- 1.1.2
- drop upstreamed gpgme-1.1.0-tests.patch

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- fc5: gcc/glibc respin

* Wed Nov 30 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 1.1.0-3
- (re)build against (newer) libksba/gnupg2

* Thu Oct 06 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 1.1.0-2
- 1.1.0

* Mon Aug  8 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 1.0.3-1
- 1.0.3
- --disable-static

* Thu May 12 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2-3
- rebuilt

* Fri Mar 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-2
- Fix FC4 build.

* Tue Feb  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:1.0.2-1
- LGPL used here, and made summary more explicit.
- Remove dirmngr dependency (gpgsm interfaces with it).
- Obsolete cryptplug as gpgme >= 0.4.5 provides what we used cryptplug for.

* Thu Jan 06 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0:1.0.2-0.fdr.1
- 1.0.2

* Thu Oct 21 2004 Rex Dieter <rexdieter at sf.net> 0:1.0.0-0.fdr.1
- 1.0.0
- Requires: dirmngr

* Tue Oct 19 2004 Rex Dieter <rexdieter at sf.net> 0:0.4.7-0.fdr.1
- 0.4.7

* Sun May  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.3
- Require %%{_bindir}/gpgsm instead of newpg.
- Cosmetic spec file improvements.

* Thu Oct 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.2
- Update description.

* Tue Oct  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.1
- Update to 0.4.3.

* Fri Aug 15 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.2-0.fdr.1
- Update to 0.4.2.
- make check in the %%check section.

* Thu Jul 10 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.1-0.fdr.1
- Update to 0.4.1.
- Make -devel cooperate with --excludedocs.

* Sat Apr 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.0-0.fdr.2
- BuildRequire pth-devel, fix missing epoch in -devel Requires (#169).
- Save .spec in UTF-8.

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.0-0.fdr.1
- Update to current Fedora guidelines.
- Exclude %%{_libdir}/*.la.

* Tue Feb 12 2003 Warren Togami <warren@togami.com> 0.4.0-1.fedora.3
- info/dir temporary workaround

* Sat Feb  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.4.0-1.fedora.1
- First Fedora release.
