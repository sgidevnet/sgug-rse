%global pypi_name pytest-datafiles

Name:           python-%{pypi_name}
Version:        2.0
Release:        2%{?dist}
Summary:        A pytest plugin to create a 'tmpdir' containing predefined content

License:        MIT
URL:            https://github.com/omarkohl/pytest-datafiles
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This plugin allows you to specify one or several files/directories that are
copied to a temporary directory (tmpdir) before the execution of the test.
This means the original files are not modified and every test runs on its
own version of the same files.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-py
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This plugin allows you to specify one or several files/directories that are
copied to a temporary directory (tmpdir) before the execution of the test.
This means the original files are not modified and every test runs on its
own version of the same files.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests
rm -rf %{buildroot}%{python3_sitelib}/__pycache__/pytest_datafiles.cpython-*-PYTEST.pyc


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_datafiles.py
%{python3_sitelib}/pytest_datafiles-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0-1
- Initial package for Fedora
