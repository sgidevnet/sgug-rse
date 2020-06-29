%global srcname threadpoolctl

Name: python-%{srcname}
Version: 2.0.0
Release: 3%{?dist}
Summary: Thread-pool Controls
License: BSD

URL: https://github.com/joblib/threadpoolctl
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
Python helpers to limit the number of threads used in the 
threadpool-backed of common native libraries used for scientific computing 
and data science (e.g. BLAS and OpenMP).
Fine control of the underlying thread-pool size can be useful in 
workloads that involve nested parallelism so as to mitigate 
oversubscription issues.}     

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-devel 
# Testing
BuildRequires: python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
pytest -v

%files -n python3-%{srcname}
%doc README.md multiple_openmp.md
%license LICENSE
%pycached %{python3_sitelib}/threadpoolctl.py
%{python3_sitelib}/threadpoolctl*egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu May 21 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0.0-2
- Package approved

* Tue May 19 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0.0-1
- Initial spec
