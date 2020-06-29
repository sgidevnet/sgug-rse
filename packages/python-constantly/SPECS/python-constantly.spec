# Created by pyp2rpm-3.3.2
%global pypi_name constantly

%global common_description %{expand:
A library that provides symbolic constant support. It includes collections and
constants with text, numeric, and bit flag values. Originally
twisted.python.constants from the Twisted project.}

Name:           python-%{pypi_name}
Version:        15.1.0
Release:        10%{?dist}
Summary:        Symbolic constants in Python

License:        MIT
URL:            https://github.com/twisted/constantly
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 15.1.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 23:11:50 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 15.1.0-8
- Drop Python 2 support (#1761209)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 15.1.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 15.1.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 15.1.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 15.1.0-1
- Initial package.
