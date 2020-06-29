%global desc %{expand: \
Numpoly is a generic library for creating, manipulating and evaluating arrays of polynomials.}

%global pypi_name numpoly

Name:		python-%{pypi_name}
Version:	1.0.3
Release:	1%{?dist}
Summary:	Polynomials as a numpy datatype
License:	BSD
URL:		https://github.com/jonathf/numpoly

# Use the github source to build this package.
Source0:	%{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)
BuildRequires:	pyproject-rpm-macros
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3-sympy
BuildRequires:	pylint
BuildRequires:	python3-six
BuildRequires:	poetry
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pytest-cov)
BuildRequires:	python3dist(coverage)
BuildRequires:	python3dist(pydocstyle)
BuildRequires:	python3dist(wheel)

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

#%check
#export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
#pytest-%{python3_version} test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Fri Jun 26 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.0.3-1
- New upstream version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.2.3-2
- New upstream version

* Wed Apr 22 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.1.16-2
- Fix comments in BZ1808552

* Wed Apr 22 2020 Luis Bazan <lbazan@fedoraproject.org> - 0.1.16-1
- Initial Import
