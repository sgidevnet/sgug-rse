%global pypi_name rfc3987

Name:		python-%{pypi_name}
Version:	1.3.7
Release:	14%{?dist}
Summary:	Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)

License:	GPLv3+
URL:		https://github.com/dgerber/rfc3987
Source0:	https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

%global _description \
This module provides regular expressions according to RFC 3986 "Uniform\
Resource Identifier (URI): Generic Syntax" <http://tools.ietf.org/html/rfc3986>\
and RFC 3987 "Internationalized Resource Identifiers (IRIs)"\
<http://tools.ietf.org/html/rfc3987>, and utilities for composition and\
relative resolution of references.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:	Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:	python3-setuptools
BuildRequires:	python3-devel

%description -n python3-%{pypi_name} %{_description}

This package includes the Python 3 version of the module.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Remove shebang
sed -i -e '/^#!\//, 1d' %{buildroot}%{python3_sitelib}/rfc3987.py

%check
%{__python3} -m doctest -v %{pypi_name}.py


%files -n python3-%{pypi_name}
%license COPYING.txt
%doc README.txt
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitelib}/__pycache__/%{pypi_name}.*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.7-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.7-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.7-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.7-2
- Remove shebang from rfc3987.py

* Tue Apr 11 2017 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.7-1
- Update to 1.3.7
- Include license text from tarball

* Wed Dec 21 2016 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.6-2
- Call doctest in %%check

* Mon Jul 18 2016 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.3.6-1
- Initial packaging
