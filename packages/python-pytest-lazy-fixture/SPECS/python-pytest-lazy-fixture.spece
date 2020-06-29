# Enabled by default
%bcond_without tests

%global pypi_name pytest-lazy-fixture

%global _description %{expand:
Use fixtures in pytest.mark.parametrize.}

Name:           python-%{pypi_name}
Version:        0.5.2
Release:        8%{?dist}
Summary:        Use fixtures in pytest.mark.parametrize

# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source %{pypi_name}

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist setuptools}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH="%{buildroot}/%{python3_sitelib}/" pytest-3
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_lazy_fixture-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/pytest_lazyfixture.py
%{python3_sitelib}/__pycache__

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.2-2
- Re-enable tests

* Fri Jul 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.2-1
- Own pycache directory to fix permission issues #1723047

* Sat Jun 22 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.2-1
- Initial package
