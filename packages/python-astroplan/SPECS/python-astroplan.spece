
%global srcname astroplan

Name:           python-%{srcname}
Version:        0.6
Release:        3%{?dist}
Summary:        Python package to help astronomers plan observations

License:        BSD
URL:            https://pypi.org/project/astroplan/
Source0:        %{pypi_source}

BuildArch:      noarch


%global _description %{expand:
astroplan is an observation planning package for 
astronomers that can help you plan for everything but the clouds.

It is an in-development Astropy affiliated package that seeks to make your 
life as an observational astronomer a little less infuriating.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# For testing
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist astropy}
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist pytest-astropy}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist astroquery}
%{?python_provide:%python_provide python3-%{srcname}}
Recommends: %{py3_dist matplotlib}
Recommends: %{py3_dist astroquery}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}/%{python3_sitelib}
   pytest-%{python3_version} --remote-data=none astroplan || :
popd


%files -n python3-%{srcname}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.6-1
- New release 0.6

* Sat Dec 07 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.5-2
- Fix project url
- Add check section

* Mon Nov 11 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.5-1
- Initial spec file

