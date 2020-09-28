%global apiversion 0.14

Name: libixion
Version: 0.14.1
Release: 4%{?dist}
Summary: A general purpose formula parser & interpreter library

License: MPLv2.0
URL: https://gitlab.com/ixion/ixion
Source0: http://kohei.us/files/ixion/src/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: pkgconfig(mdds-1.4)
BuildRequires: pkgconfig(python3)

%description
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

The goal of this project is to create a library for calculating the results of
formula expressions stored in multiple named targets, or “cells”. The cells can
be referenced from each other, and the library takes care of resolving their
dependencies automatically upon calculation. The caller can run the calculation
routine either in a single-threaded mode, or a multi-threaded mode. The library
also supports re-calculations where the contents of one or more cells have been
modified since the last calculation, and a partial calculation of only the
affected cells need to be calculated.

Supported features:
- Each calculation session is defined in a plain text file, which is parsed and
  interpreted by the Ixion parser.
- Fully threaded calculation.
- Name resolution using A1-style references.
- Support 2D cell references and named expressions.
- Support range references.
- Dependency tracking during both full calculation and partial re-calculation.
- Inline strings.
- Volatile functions. The framework for volatile functions is implemented. We
  just need to implement more functions.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Testing tools for libixion
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Testing tools for %{name}.

%package python3
Summary: Python 3 bindings for libixion
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < 0.9.1-1
Suggests: %{name}-doc = %{version}-%{release}

%description python3
Python 3 bindings for %{name}.

#%%package doc
#Summary: API documentation for #%%{name}
#BuildArch: noarch

#%%description doc
#API documentation for #%%{name}.

%prep
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{python3_sitearch}/*.la

# create and install man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
#help2man -S '%{name} %{version}' -N -n 'formula tokenizer' -o ixion-formula-tokenizer.1 ./src/ixion-formula-tokenizer
#help2man -S '%{name} %{version}' -N -n 'parser' -o ixion-parser.1 ./src/ixion-parser
#help2man -S '%{name} %{version}' -N -n 'sorter' -o ixion-sorter.1 ./src/ixion-sorter
#install -m 0755 -d %{buildroot}/%{_mandir}/man1
#install -m 0644 ixion-*.1 %{buildroot}/%{_mandir}/man1

# generate docs
# make doc

#%%ldconfig_scriptlets

%check
#export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export LD_LIBRARYN32_PATH=%{buildroot}%{_libdir}
make %{?_smp_mflags} check

%files
%doc AUTHORS
%license LICENSE
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files tools
%{_bindir}/ixion-formula-tokenizer
%{_bindir}/ixion-parser
%{_bindir}/ixion-sorter
#%%{_mandir}/man1/ixion-formula-tokenizer.1*
#%%{_mandir}/man1/ixion-parser.1*
#%%{_mandir}/man1/ixion-sorter.1*

%files python3
%{python3_sitearch}/ixion.so

#%%files doc
#%%license LICENSE
#%%doc doc/python

%changelog
* Mon Sep 28 2020  HAL <notes2@gmx.de> - 0.14.1-4
- compiles on Irix 6.5 with sgug-rse gcc 9.2. Passing all tests.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.14.1-2
- Rebuilt for Boost 1.69

* Fri Oct 26 2018 David Tardon <dtardon@redhat.com> - 0.14.1-1
- new upstream release

* Sun Sep 02 2018 David Tardon <dtardon@redhat.com> - 0.14.0-1
- new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.13.0-2
- Rebuilt for Boost 1.66

* Wed Oct 11 2017 David Tardon <dtardon@redhat.com> - 0.13.0-1
- new upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.12.2-5
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.12.2-3
- Rebuilt for Boost 1.63

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.2-2
- Rebuild for Python 3.6

* Thu Dec 15 2016 David Tardon <dtardon@redhat.com> - 0.12.2-1
- new upstream release

* Mon Sep 26 2016 David Tardon <dtardon@redhat.com> - 0.12.1-1
- new upstream release

* Wed Jul 20 2016 David Tardon <dtardon@redhat.com> - 0.12.0-1
- new upstream release

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 12 2016 David Tardon <dtardon@redhat.com> - 0.11.1-1
- new upstream release

* Fri Mar 11 2016 David Tardon <dtardon@redhat.com> - 0.11.0-2
- build python documentation

* Sun Feb 14 2016 David Tardon <dtardon@redhat.com> - 0.11.0-1
- new upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-7
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.9.1-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 David Tardon <dtardon@redhat.com> - 0.9.1-2
- rebuild for yet another C++ ABI break

* Sun Apr 05 2015 David Tardon <dtardon@redhat.com> - 0.9.1-1
- new upstream release

* Thu Mar 05 2015 David Tardon <dtardon@redhat.com> - 0.9.0-2
- fix python bindings on i386

* Wed Feb 18 2015 David Tardon <dtardon@redhat.com> - 0.9.0-1
- new upstream release

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.7.0-4
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 David Tardon <dtardon@redhat.com> - 0.7.0-1
- initial import
