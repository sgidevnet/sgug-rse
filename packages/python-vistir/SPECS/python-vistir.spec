%global srcname vistir
%global _description %{expand:
Miscellaneous utilities for dealing with filesystems,
paths, projects, sub-processes, and more.}

Name:           python-vistir
Version:        0.4.3
Release:        6%{?dist}
License:        ISC
URL:            https://pypi.org/project/%{srcname}
Source0:        https://github.com/sarugaku/%{srcname}/archive/%{version}.tar.gz
BuildArch:      noarch
Summary:        Python library full of utility functions

%{?python_enable_dependency_generator}

%description
%{_description}

# one test require internet to pass
%bcond_with internet

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-invoke
BuildRequires:  python3-parver
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-yaspin
BuildRequires:  python3-requests
BuildRequires:  python3-colorama
BuildRequires:  python3-hypothesis
BuildRequires:  python3-hypothesis-fspaths
BuildRequires:  python3-pytest-timeout

# for support of spinners
Recommends:     python3-yaspin

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest tests/ \
%if %{without internet}
-k 'not test_open_file'
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Patrik Kopkan <pkopkan@redhat.com> - 0.4.3-1
- created package
