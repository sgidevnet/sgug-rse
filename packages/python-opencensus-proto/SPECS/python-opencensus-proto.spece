%global srcname opencensus-proto
%global _description %{expand:Census provides a framework to define and collect stats against metrics and to
break those stats down across user-defined dimensions.

The Census framework is natively available in many languages (e.g. C++, Go, and
Java). The API interface types are defined using protos to ensure consistency
and interoperability for the different implementations.}

Name:           python-opencensus-proto
Version:        0.2.1
Release:        2%{?dist}
Summary:        Language Independent Interface Types For OpenCensus

License:        ASL 2.0
URL:            https://github.com/census-instrumentation/%{srcname}/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        Python library generated from OpenCensus cross-language protos
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}.


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
pushd gen-python/
%py3_build
popd


%install
pushd gen-python/
%py3_install
popd


%files -n python3-%{srcname}
%doc AUTHORS CONTRIBUTING.md gen-python/README.rst
%license LICENSE
%exclude %{python3_sitelib}/opencensus/{*.py,__pycache__/}
%{python3_sitelib}/opencensus/proto/
%{python3_sitelib}/opencensus_proto-*.egg-info/


%changelog
* Sun May 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.1-2
- Rebuild for Python 3.9

* Fri May 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.1-1
- Initial RPM release
