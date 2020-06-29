%global pypi_name wurlitzer

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        4%{?dist}
Summary:        Capture C-level output in context managers

License:        MIT
URL:            https://github.com/minrk/wurlitzer
Source0:        %pypi_source
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(mock)

%description
Capture C-level stdout/stderr pipes in Python via os.dup2.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Capture C-level stdout/stderr pipes in Python via os.dup2.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
pytest test.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.3-2
- Use pypi_source macro
- Enable tests

* Sun Sep 15 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.3-1
- Initial package.
