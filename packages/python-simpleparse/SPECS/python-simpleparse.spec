%global oname   SimpleParse

Name:           python-simpleparse
License:        BSD
Summary:        A simple and fast parser generator
Version:        2.2.2
Release:        1%{?dist}
URL:            http://launchpad.net/simpleparse
Source0:        https://pypi.io/packages/source/S/SimpleParse/%{oname}-%{version}.tar.gz
Patch0:         pytuple_check.patch
BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description\
SimpleParse is a BSD-licensed Python package providing a simple and fast parser\
generator using a modified version of the mxTextTools text-tagging engine.\
SimpleParse allows you to generate parsers directly from your EBNF grammar.\
\
\

%description %_description

%package -n python3-simpleparse
Summary:        %summary
%{?python_provide:%python_provide python3-simpleparse}

%description -n python3-simpleparse %_description

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-simpleparse
%license license.txt
%doc docs
%{python3_sitearch}/*

%changelog
* Thu Jun 11 2020 Maurizio Lombardi <mlombard@redhat.com> - 2.2.2-1
- Update to version 2.2.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Jan Beran <jberan@redhat.com> - 2.2.0-1
- New version including Python 3 subpackage

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.1-17
- Python 2 binary package renamed to python2-simpleparse
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.1.1-14
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 2.1.1-3
- Add patch to fix some missing EOLs

* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 2.1.1-2
- Filter out mxtexttools.so provides

* Tue Aug 16 2011 Andy Grover <agrover@redhat.com> - 2.1.1-1
- Update to latest upstream version
- Modify URL and Source
- Remove mx dependency

* Tue May 10 2011 Andy Grover <agrover@redhat.com> - 2.0.0-1
- Initial packaging
