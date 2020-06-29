%global _short_name bitmath
%global _short_release 1

Name: python-bitmath
Summary: Aids representing and manipulating file sizes in various prefix notations
Version: 1.3.1
Release: %{_short_release}%{?dist}.15

License: BSD
Source0: https://github.com/tbielawa/bitmath/archive/%{version}.%{_short_release}.tar.gz
Url: https://github.com/tbielawa/bitmath

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools

%description
bitmath simplifies many facets of interacting with file sizes in
various units. Examples include: converting between SI and NIST prefix
units (GiB to kB), converting between units of the same type (SI to
SI, or NIST to NIST), basic arithmetic operations (subtracting 42KiB
from 50GiB), and rich comparison operations (1024 Bytes == 1KiB),
bitwise operations, sorting, automatic best human-readable prefix
selection, and completely customizable formatting.

In addition to the conversion and math operations, bitmath provides
human readable representations of values which are suitable for use in
interactive shells as well as larger scripts and applications. It can
also read the capacity of system storage devices. bitmath can parse
strings (like "1 KiB") into proper objects and has support for
integration with the argparse module as a custom argument type and the
progressbar module as a custom file transfer speed widget.

bitmath is thoroughly unittested, with almost 200 individual tests (a
number which is always increasing). bitmath's test-coverage is almost
always at 100%.

######################################################################
# Sub-package setup
%package -n python3-bitmath
Summary: Aids representing and manipulating file sizes in various prefix notations
%{?python_provide:%python_provide python3-bitmath}

%description -n python3-bitmath
bitmath simplifies many facets of interacting with file sizes in
various units. Examples include: converting between SI and NIST prefix
units (GiB to kB), converting between units of the same type (SI to
SI, or NIST to NIST), basic arithmetic operations (subtracting 42KiB
from 50GiB), and rich comparison operations (1024 Bytes == 1KiB),
bitwise operations, sorting, automatic best human-readable prefix
selection, and completely customizable formatting.

In addition to the conversion and math operations, bitmath provides
human readable representations of values which are suitable for use in
interactive shells as well as larger scripts and applications. It can
also read the capacity of system storage devices. bitmath can parse
strings (like "1 KiB") into proper objects and has support for
integration with the argparse module as a custom argument type and the
progressbar module as a custom file transfer speed widget.

bitmath is thoroughly unittested, with almost 200 individual tests (a
number which is always increasing). bitmath's test-coverage is almost
always at 100%.

######################################################################
%check
# We can't run the progressbar and argparse tests in python3 until
# progressbar has a python3 package available :(
#
# Skip those tests for now and run the rest
nosetests-%{python3_version} -e 'test_FileTransferSpeed' \
                             -e 'test_BitmathType_' \
                             -I '.*test_argparse_type.py' \
                             -I '.*test_progressbar.py' -v


######################################################################
%prep
%setup -n bitmath-%{version}.%{_short_release} -q

######################################################################
%build
%py3_build

######################################################################
%install
%py3_install


mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
cp -v *.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}/docs
cp -v -r docsite/source/* $RPM_BUILD_ROOT/%{_docdir}/%{name}/docs/
rm -f $RPM_BUILD_ROOT/%{_docdir}/%{name}/docs/NEWS.rst

######################################################################
%files -n python3-bitmath
%{python3_sitelib}/*
%doc README.rst NEWS.rst LICENSE
%doc %{_mandir}/man1/bitmath.1*
%doc %{_docdir}/%{name}/docs/
%{_bindir}/bitmath

######################################################################
%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-1.15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-1.13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-1.12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-1.9
- Subpackage python2-bitmath has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-1.7
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.1-1.6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-1.2
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-1.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 17 2016 Tim Bielawa <tbielawa@redhat.com> - 1.3.1-1
- New release

* Tue Jan 12 2016 Tim Bielawa <tbielawa@redhat.com> - 1.3.0-2
- Packaging update

* Fri Jan  8 2016 Tim Bielawa <tbielawa@redhat.com> - 1.3.0-1
- Fix best_prefix for negative values GitHub: #55

* Tue Dec 29 2015 Tim Bielawa <tbielawa@redhat.com> - 1.2.4-3
- Fix tests to run on koji
- Minor packaging changes

* Mon Nov 30 2015 Tim Bielawa <tbielawa@redhat.com> - 1.2.4-1
- New release. Now builds dual python2.x and 3.x packages.
- New function: query_device_capacity
- Minor bug fixes for everyone!

* Sun Jan  4 2015 Tim Bielawa <tbielawa@redhat.com> - 1.2.3-3
- Add mock to build requires

* Sun Jan  4 2015 Tim Bielawa <tbielawa@redhat.com> - 1.2.3-2
- Add python-progressbar build-dependency to satisfy 'check' tests

* Sun Jan  4 2015 Tim Bielawa <tbielawa@redhat.com> - 1.2.3-1
- Add progressbar example to the README

* Sun Jan  4 2015 Tim Bielawa <tbielawa@redhat.com> - 1.2.2-1
- Fix some problems with the automated build system

* Sun Jan  4 2015 Tim Bielawa <tbielawa@redhat.com> - 1.2.1-1
- Add a new integration: the progressbar module FileTransferSpeed widget

* Mon Dec 29 2014 Tim Bielawa <tbielawa@redhat.com> - 1.2.0-1
- Add argparse integration with a BitmathType argument type

* Sat Dec 20 2014 Tim Bielawa <tbielawa@redhat.com> - 1.1.0-1
- New parse_string utility function from tonycpsu
- 'bitmath' tool added for converting on the command line

* Fri Aug 15 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.8-3
- Actually fix this whole specfile and version mixup

* Fri Aug 15 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.8-2
- Fix macro expansion in specfile changelog

* Thu Aug 14 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.8-1
- First release with contributors: davidfischer-ch and hikusukih! Thank you!
- Real documentation (via readthedocs.org)
- Significant formatting functionality added:
- +formatting context manager, listdir, getsize
- Python3 compat via rtruediv contribution!
- So many more unit tests
- Coveralls code-coverage review
- Pluralization/singularity in string formatting (thanks for the contribution!)

* Sat Jul 19 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.7-1
- Lots of documentation and unittest updates
- See GitHub Milestone 2: 1.0.7 for a list of closed issues

* Mon Jul 14 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.6-1
- New instance properties
- Custom representation formatting method. #9
- Best-prefix guessing: select the best human-readable prefix unit
  automatically. #6
- Bitwise operation support. #3
- More unittests than your body has room for

* Mon Apr 28 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.5-1
- Now with support for bitwise operations

* Thu Mar 20 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.4-1
- Plenty of documentation updates
- Fix some issues with mix-type math operations.
- More unit tests!

* Mon Mar 17 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.3-1
- Big issue converting NIST to SI
- Also, retroactively remove unexpanded macros from changelog

* Thu Mar 13 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.2-3
- Bump release for new archive format

* Thu Mar 13 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.2-2
- Bump spec for proper Source0 versioning

* Thu Mar 13 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.2-1
- First real solid release with full functionality and documentation

* Tue Mar 11 2014 Tim Bielawa <tbielawa@redhat.com> - 1.0.0-1
- First release
