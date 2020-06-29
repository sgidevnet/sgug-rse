%global srcname pynetbox

Name:           python-%{srcname}
Version:        4.3.1
Release:        2%{?dist}
Summary:        Python API client library for Netbox

License:        ASL 2.0
URL:            https://github.com/digitalocean/pynetbox
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  (python3dist(requests) >= 2.20 with python3dist(requests) < 3)
BuildRequires:  (python3dist(six) >= 1 with python3dist(six) < 2)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install
rm -vr %{buildroot}%{python3_sitelib}/tests

%check
%python3 -m unittest discover

%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-2
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1

* Tue Feb 11 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.2.5-1
- Update to 4.2.5

* Thu Jan 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 4.2.4-1
- Initial package
