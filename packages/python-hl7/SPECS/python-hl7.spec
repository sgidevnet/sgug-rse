
%global srcname hl7
%global sum  Python library parsing HL7 v2.x and v3.x messages

Name:           python-%{srcname}
Version:        0.3.3
Release:        19%{?dist}
# append my cmake path before swig is included
Summary:        Python library parsing HL7 v2.x and v3.x messages

License:        BSD
URL:            http://pypi.python.org/pypi/%{srcname}

Source0:        %{pypi_source %{srcname}}
Source1:        https://raw.githubusercontent.com/johnpaulett/python-hl7/master/AUTHORS

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools

%description
python-%{srcname} is a simple library for parsing messages of
Health Level 7 (HL7) v2.x into Python objects.

%package -n python3-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python-%{srcname} is a simple library for parsing messages of
Health Level 7 (HL7) v2.x into Python objects.

%package doc
Summary: Documentation for %{srcname}

%description doc
Documentation files for %{srcname}

%prep
%setup -q  -n %{srcname}-%{version}
rm -rf *egg-info
cp %{SOURCE1} .

%build

# Make docs
# These modes appear to be enough
pushd docs/
    make html
    make singlehtml
    make man
    make htmlhelp
popd

%py3_build

%install
%py3_install

# Delete buildinfo file
find docs/_build/ -name ".buildinfo" -execdir rm -fv '{}' \;

%files -n python3-%{srcname}
%{_bindir}/mllp_send
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%license LICENSE

%files doc
%doc docs/_build/html docs/_build/htmlhelp docs/_build/singlehtml README.rst AUTHORS
%license LICENSE

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.3-19
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-13
- Subpackage python2-hl7 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.3-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.3.3-1
- Update to latest upstream version
- Build python3 version
- Separate doc subpackage
- mmlp_send is py3 only

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-3
- spec bump for gcc 4.7 rebuild

* Thu Jul 21 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-2
- Correct description
- Make additional docs

* Sun Jul 17 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-1
- Use the original source

* Thu Jul 14 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.1_xml.4-0.1.20110714git97ddbe9
- Initial rpm build
