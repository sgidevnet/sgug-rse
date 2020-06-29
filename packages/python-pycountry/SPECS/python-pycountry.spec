%global srcname pycountry

Name:           python-%{srcname}
Version:        19.8.18
Release:        5%{?dist}
Summary:        ISO country, subdivision, language, currency and script definitions and their translations

License:        LGPLv2
URL:            https://github.com/flyingcircusio/pycountry
Source0:        %pypi_source
# Rebased from Debian:
Patch0001:      00-use_system_iso-codes.patch
# https://github.com/flyingcircusio/pycountry/pull/16 (partially)
Patch0002:      https://github.com/flyingcircusio/pycountry/pull/16/commits/1979282ee3cc6b1955240dbea46843832e9afc3a.patch
Patch0003:      support-iso-codes-450.patch

BuildArch:      noarch

BuildRequires:  iso-codes >= 4.1
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description
pycountry provides the ISO databases for the standards:
* 639-3 Languages
* 3166 Countries
* 3166-3 Deleted countries
* 3166-2 Subdivisions of countries
* 4217 Currencies
* 15924 Scripts


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       iso-codes >= 4.1

%description -n python3-%{srcname}
pycountry provides the ISO databases for the standards:
* 639-3 Languages
* 3166 Countries
* 3166-3 Deleted countries
* 3166-2 Subdivisions of countries
* 4217 Currencies
* 15924 Scripts


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf src/%{srcname}.egg-info

# Remove bundled iso-codes data
rm -rf src/%{srcname}/{databases,locales}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 \
    %{python3} -m pytest --pyargs pycountry


%files -n python3-%{srcname}
%doc README.rst HISTORY.txt
%license LICENSE.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info


%changelog
* Wed May 27 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 19.8.18-5
- Support iso-codes 4.5

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 19.8.18-5
- Rebuilt for Python 3.9

* Sun Feb 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 19.8.18-4
- Update upstream URL
- Backport patch to build with iso-codes 4.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.8.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.8.18-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 19.8.18-1
- Update to latest version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 18.12.8-1
- Initial package.
