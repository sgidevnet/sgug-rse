%{?python_enable_dependency_generator}

%global srcname Python-fontconfig

Name:           python-fontconfig
Version:        0.5.1
Release:        3%{?dist}
Summary:        Python bindings for Fontconfig library

License:        GPLv3
URL:            https://pypi.org/project/Python-fontconfig/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  fontconfig-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
# Needed for tests
BuildRequires:  gnu-free-mono-fonts

%description
%{summary}.


%package -n python3-fontconfig
Summary:        %{summary}
%{?python_provide:%python_provide python3-fontconfig}

%description -n python3-fontconfig
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{__python3} setup.py build_ext -i
%py3_build


%install
%py3_install


%check
export PYTHONPATH=$PWD/build/lib.%{python3_platform}-%{python3_version}/
yes | %{__python3} test/test.py


%files -n python3-fontconfig
%doc README.rst
%license LICENSE.txt
%{python3_sitearch}/*.so
%{python3_sitearch}/*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.5.1-1
- Initial RPM release
