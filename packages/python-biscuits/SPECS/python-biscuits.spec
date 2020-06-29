%global pypi_name biscuits

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        5%{?dist}
Summary:        Fast and tasty cookies handling

License:        MIT
URL:            https://github.com/pyrates/%{pypi_name}
Source0:        https://github.com/pyrates/%{pypi_name}/archive/%{version}/%{name}-%{version}.tar.gz

# The upstream makefile calls python directly, but we want to be able to pass
# in a particular interpreter
Patch0:         0000-makefile-python-param.patch

BuildRequires:  gcc
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3dist(setuptools)

%description
Low level API for handling cookies.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Low level API for handling cookies.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
make compile PYTHON=%{__python3}
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -v

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitearch}/biscuits.cpython-%{python3_version_nodots}*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Eli Young <elyscape@gmail.com> - 0.2.1-1
- Initial import (#1687620)
