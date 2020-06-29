%global srcname uamqp
%global _description %{expand:An AMQP 1.0 client library for Python.}

Name:           python-%{srcname}
Version:        1.2.8
Release:        2%{?dist}
Summary:        AMQP 1.0 client library for Python

License:        MIT
URL:            https://github.com/Azure/azure-uamqp-python/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist setuptools}
# Required for tests
BuildRequires:  %{py3_dist certifi}
BuildRequires:  %{py3_dist pytest}

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n azure-uamqp-python-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=strict-aliasing"
export CXXFLAGS=$CFLAGS
VERBOSE=1 %py3_build


%install
%py3_install

rm $RPM_BUILD_ROOT%{python3_sitearch}/%{srcname}/*.c


%check
PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitearch}/ pytest-%{python3_version} tests


%files -n python3-%{srcname}
%doc HISTORY.rst README.rst
%license LICENSE
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info/


%changelog
* Sun May 31 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.8-2
- Rebuild for Python 3.9

* Fri May 29 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2.8-1
- Initial RPM release
