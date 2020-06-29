# Created by pyp2rpm-3.3.2
%global pypi_name portend
%global with_docs 1
%{?python_enable_dependency_generator}

Name:           python-%{pypi_name}
Version:        2.6
Release:        3%{?dist}
Summary:        TCP port monitoring utilities

License:        MIT
URL:            https://github.com/jaraco/portend
Source0:        %{pypi_source}
BuildArch:      noarch
 
%description
 por·tend pôrˈtend/ be a sign or warning that (something, especially something
momentous or calamitous) is likely to happen.

%package -n python3-%{pypi_name}
Summary:        portend documentation

BuildRequires:  python3-devel
BuildRequires:  python3dist(jaraco.functools)
BuildRequires:  python3dist(pytest) >= 3.4
BuildRequires:  python3dist(pytest-cov)
%{?fedora:BuildRequires: python3dist(pytest-flake8)}
#BuildRequires:  python3dist(pytest-sugar) >= 0.9.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15
BuildRequires:  python3dist(tempora) >= 1.8

%description -n python3-%{pypi_name}
 por·tend pôrˈtend/ be a sign or warning that (something, especially something
momentous or calamitous) is likely to happen.

%if 0%{?with_docs}
%package -n python-%{pypi_name}-doc
Summary:        portend documentation

BuildRequires:  python3dist(jaraco.packaging) >= 3.2
BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-more-itertools

%description -n python-%{pypi_name}-doc
Documentation for portend
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# black is apparently not a valid option?
sed -i 's/ --black//' pytest.ini

%build
%py3_build

%if 0%{?with_docs}
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
%if 0%{?el8}
# disable flake8 in the tests, need a newer version of pytest (3.5) which is not
# available on EL8, and is pulled in by python-pytest-flake8.
sed -i 's/ --flake8//' pytest.ini
%endif
LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Dan Radez <dradez@redhat.com> - 2.6-1
- update to 2.6
- reenable flake8
- add coverage build dep

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Dan Radez <dradez@redhat.com> - 2.5-1
- Update to 2.5

* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 2.3-1
- Initial package.
