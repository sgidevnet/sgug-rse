%bcond_without check
%global pypi_name zstandard
%if 0%{!?pytest:1}
%global pytest %{expand:\\\
  CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\\\
  PATH="%{buildroot}%{_bindir}:$PATH"\\\
  PYTHONPATH="${PYTHONPATH:-%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}}"\\\
  PYTHONDONTWRITEBYTECODE=1\\\
  /usr/bin/pytest}
%endif

%global desc This project provides Python bindings for interfacing with the Zstandard\
compression library. A C extension and CFFI interface are provided.

Name: python-%{pypi_name}
Version: 0.13.0
Release: 1%{?dist}
Summary: Zstandard bindings for Python
License: BSD
URL: https://github.com/indygreg/python-zstandard
Source0: %{pypi_source}

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: gcc
BuildRequires: libzstd-devel
BuildRequires: python3-devel
BuildRequires: python3-cffi
%if %{with check}
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
%endif
# https://github.com/indygreg/python-zstandard/issues/48
Provides: bundled(zstd) = 1.4.4

%description -n python3-%{pypi_name}
%{desc}

%prep
%setup -q -n %{pypi_name}-%{version}
rm -r %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
export ZSTD_SLOW_TESTS=1
%pytest -v\
%ifarch s390x
        -k 'not test_constant_methods\
        and not test_no_context_manager\
        and not test_read_closed\
        and not test_close\
        and not test_read_after_exit\
        and not test_read_buffer\
        and not test_read_stream'\
%endif
        --numprocesses=auto
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc NEWS.rst README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/_zstd_cffi.cpython-%{python3_version_nodots}-%{_arch}-linux%{_gnu}.so
%{python3_sitearch}/zstd.cpython-%{python3_version_nodots}-%{_arch}-linux%{_gnu}.so

%changelog
* Fri May 29 2020 Dominik Mierzejewski <dominik@greysector.net> 0.13.0-1
- initial build
- skip some tests on s390x (https://github.com/indygreg/python-zstandard/issues/105)

