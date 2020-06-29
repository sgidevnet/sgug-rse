

%global srcname arviz

Name:           python-%{srcname}
Version:        0.9.0
Release:        1%{?dist}
Summary:        Exploratory analysis of Bayesian models

License:        ASL 2.0
URL:            https://arviz-devs.github.io/arviz/
Source0:        %{pypi_source}

BuildArch:      noarch


%global _description %{expand:
ArviZ is a Python package for exploratory analysis of Bayesian models. 
Includes functions for posterior analysis, sample diagnostics, 
model checking, and comparison.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
# The benchmarks directory it's installed, exclude it
%exclude %{python3_sitelib}/benchmarks/

%changelog
* Sun Jun 28 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.0-1
- New upstream release (0.9.0)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.9

* Sat May 23 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.0-1
- New upstream release (0.8.0)

* Mon Mar 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.7.0-1
- New upstream release (0.7.0)

* Sun Feb 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.6.1-1
- New upstream release (0.6.1)

* Mon Nov 11 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.5.1-1
- Initial spec file

