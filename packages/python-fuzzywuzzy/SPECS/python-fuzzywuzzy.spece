%global pypi_name fuzzywuzzy

Name:           python-%{pypi_name}
Version:        0.18.0
Release:        3%{?dist}
Summary:        Fuzzy string matching in Python

License:        MIT
URL:            https://github.com/seatgeek/fuzzywuzzy/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Fuzzy string matching module that uses Levenshtein Distance to calculate the
differences between sequences in a simple-to-use package.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pycodestyle
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Fuzzy string matching module that uses Levenshtein Distance to calculate the
differences between sequences in a simple-to-use package.

%prep
%setup -q -n %{pypi_name}-%{version}
# These scripts shouldn't be executable
sed -i '1d' %{pypi_name}/{fuzz.py,process.py,StringMatcher.py}
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py3_build


%install
%py3_install

%check
%{__python3} -m unittest

%files -n python3-%{pypi_name}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-3
- Rebuilt for Python 3.9

* Mon Apr 06 2020 Fabian Affolter <mail@fabian-affolter.ch>  - 0.18.0-2
- Update spec file

* Sat Apr 04 2020 Christopher Tubbs <ctubbsii@fedoraproject.org> - 0.18.0-1
- New version 0.18.0 (rhbz#1244987)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-11
- Subpackage python2-fuzzywuzzy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-7
- Python 2 binary package renamed to python2-fuzzywuzzy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Slavek Kabrda <bkabrda@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Björn Esser <bjoern.esser@gmail.com> - 0.5.0-1
- Updated to version 0.5
- Use %%{python2}-macros

* Fri Nov 14 2014 Slavek Kabrda <bkabrda@redhat.com> - 0.4.0-1
- Updated to version 0.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2-1
- Updated to 0.2
- Introduced python3 subpackage
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1-2
- python-devel should be python2-devel
- URL now points to the real homepage of the project

* Fri Jun 22 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1-1
- Initial package.
