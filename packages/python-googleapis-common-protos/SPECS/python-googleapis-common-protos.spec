%global srcname googleapis-common-protos
%global _description %{summary}.

Name:           python-%{srcname}
Version:        1.52.0
Release:        1%{?dist}
Summary:        Common protobufs used in Google APIs

License:        ASL 2.0
URL:            https://github.com/googleapis/python-api-common-protos/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n python-api-common-protos-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE
%{python3_sitelib}/google/
%{python3_sitelib}/googleapis_common_protos-*.egg-info/
%{python3_sitelib}/googleapis_common_protos-*-nspkg.pth


%changelog
* Thu Jun 18 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.52.0-1
- Update to 1.52.0

* Sun May 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.51.0-2
- Rebuild for Python 3.9

* Fri May 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.51.0-1
- Initial RPM release
