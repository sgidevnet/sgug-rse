%global         pypi_name hypothesis-fspaths
%global         modulename hypothesis_fspaths
Name:           python-%{pypi_name}
Version:        0.1
Release:        6%{?dist}
License:        MIT
URL:            https://pypi.org/project/%{pypi_name}
Source0:        %{pypi_source}
BuildArch:      noarch
Summary:        Python library for generating filesystem paths

%{?python_enable_dependency_generator}

%description
Hypothesis extension for generating filesystem paths.
Anything the built-in Python function open() accepts can be generated.

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-hypothesis
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Hypothesis extension for generating filesystem paths.
Anything the built-in Python function open() accepts can be generated.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modulename}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{modulename}.py
%{python3_sitelib}/__pycache__/%{modulename}.*.py*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jan 8 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.1-1
- created package
