%global pypi_name pdfkit
%global commit0   6f1077dbae22863390915b6f69c8ec77f7c4a83f
%global testurl   https://raw.githubusercontent.com/JazzCore/python-%{pypi_name}/%{commit0}/tests/

Name:           python-%{pypi_name}
Version:        0.6.1
Release:        2%{?dist}
Summary:        Wkhtmltopdf python wrapper

License:        MIT
URL:            https://github.com/JazzCore/python-%{pypi_name}
Source0:        %{pypi_source}

# tests taken from github due to not part of pypi
Source10:        %{testurl}/%{pypi_name}-tests.py#/%{commit0}_pdfkit-tests.py
Source11:        %{testurl}/fixtures/example.css#/%{commit0}_example.css
Source12:        %{testurl}/fixtures/example.html#/%{commit0}_example.html
Source13:        %{testurl}/fixtures/example2.css#/%{commit0}_example2.css

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3
BuildRequires:  python3-pytest
BuildRequires:  wkhtmltopdf

Requires:       wkhtmltopdf

%description
Python 2 wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit.

This is an adapted version of Ruby PDFKit.

%package -n python3-%{pypi_name}
Summary:        Wkhtmltopdf python wrapper
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python 3 wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit.

This is an adapted version of Ruby PDFKit.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
mkdir -p tests/fixtures
cp -t tests %{SOURCE10}
cp -t tests/fixtures %{SOURCE11} %{SOURCE12} %{SOURCE13}
find tests -type f |\
 while read a; do b=$(echo $a |\
 sed -r 's/%{commit0}_//'); \
 mv -v $a $b; done
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst HISTORY.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Rebuilt for Python 3.9

* Mon Mar 16 2020 Raphael Groner <projects.rg@smart.ms> - 0.6.1-1
- new version

* Mon Mar 16 2020 Raphael Groner <projects.rg@smart.ms> - 0.5.0-18
- add tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-12
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 17 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 0.5.0-1
- Update to 0.5.0
- Update python macros
- Include python 2 and 3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Fedora <williamjmorenor@gmail.com> 
- 0.4.1-7
- Define %%license macro for el6

* Sun Dec 07 2014 William José Moreno Reyes <williamjmorenor@gmail.com> - 0.4.1-6
- Add %%licence macro

* Sun Oct 19 2014 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.4.1-5
- Fix Python3  dependency

* Thu Oct 16 2014 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.4.1-4
- Fix Python3 macros in %%build 

* Fri Oct 03 2014 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.4.1-3
- Subpackage for Python3

* Tue Sep 30 2014 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.4.1-2
- Fixing %%doc macro

* Sat Sep 20 2014 William José Moreno Reyes <williamjmorenor at gmail.com> - 0.4.1-1
- Initial package.
