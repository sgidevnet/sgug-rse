%global pypi_name stdio-mgr

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        2%{?dist}
Summary:        Context manager for mocking/wrapping stdin/stdout/stderr

License:        MIT
URL:            https://www.github.com/bskinn/stdio-mgr
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
While some functionality here is more or less duplicative of redirect_stdout
and redirect_stderr in contextlib within the standard library, it provides (i)
a much more concise way to mock both stdout and stderr at the same time, and
(ii) a mechanism for mocking stdin, which is not available in contextlib.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-restview
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
While some functionality here is more or less duplicative of redirect_stdout
and redirect_stderr in contextlib within the standard library, it provides (i)
a much more concise way to mock both stdout and stderr at the same time, and
(ii) a mechanism for mocking stdin, which is not available in contextlib.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/stdio_mgr/
%{python3_sitelib}/stdio_mgr-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora
