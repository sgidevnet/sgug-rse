%global srcname grpcio-gcp
%global _description %{summary}.

Name:           python-%{srcname}
Version:        0.2.2
Release:        2%{?dist}
Summary:        gRPC for GCP extensions

License:        ASL 2.0
URL:            https://github.com/GoogleCloudPlatform/grpc-gcp-python/
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
%autosetup -n grpc-gcp-python-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
pushd src/
ln -s ../template/version.py .
%py3_build
popd


%install
pushd src/
%py3_install
popd


%files -n python3-%{srcname}
%doc src/{CHANGELOG.rst,README.md}
%license src/LICENSE
%{python3_sitelib}/grpc_gcp/
%{python3_sitelib}/grpcio_gcp-*.egg-info/


%changelog
* Sun May 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.2-2
- Rebuild for Python 3.9

* Fri May 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.2-1
- Initial RPM release
