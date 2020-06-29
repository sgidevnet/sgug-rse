%global srcname parse_type

Name:           python-%{srcname}
Version:        0.4.2
Release:        8%{?dist}
Summary:        Simplifies to build parse types based on the parse module

License:        BSD
URL:            http://pypi.python.org/pypi/parse_type
Source0:        %pypi_source

BuildArch:      noarch

%{?python_enable_dependency_generator}

%global _description \
"parse_type" extends the "parse" module (opposite of\
"string.format()") with the following features:\
* build type converters for common use cases (enum/mapping, choice)\
* build a type converter with a cardinality constraint (0..1,\
  0..*, 1..*) from the type converter with cardinality=1.\
* compose a type converter from other type converters\
* an extended parser that supports the CardinalityField naming\
  schema and creates missing type variants (0..1, 0..*, 1..*) from\
  the primary type converter

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-parse
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-sphinx >= 1.1

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%setup -q -n %{srcname}-%{version}
rm -vrf *.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Remove python2 subpackage

* Wed Aug 22 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-1
- Update to 0.4.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-17
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.4-16
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-12
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.4-10
- Correctly do Provides/Obsoletes

* Sun May  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.4-9
- Provide/Obsolete python-parse_type for upgrade paths

* Tue Apr 19 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.4-8
- Use %%license
- Use %%python_provide
- Don't use splitted dirs
- Correctly split python2- subpkg
- Other cleanups/fixes

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Matěj Cepl <mcepl@redhat.com> - 0.3.4-6
- Whoops! Duplicated BuildRequires and Requires removed.

* Tue Dec 15 2015 Matěj Cepl <mcepl@redhat.com> - 0.3.4-5
- Remove unnecessary dependency on python-enum34 for python3 (#1286457)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 19 2014 Matěj Cepl <mcepl@redhat.com> - 0.3.4-1
- initial package for Fedora
