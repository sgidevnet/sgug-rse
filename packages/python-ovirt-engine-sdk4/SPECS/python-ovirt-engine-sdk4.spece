%global srcname ovirt-engine-sdk-python

Name: python-ovirt-engine-sdk4
Summary: Python SDK for version 4 of the oVirt Engine API
Version: 4.3.2
%global major_version %(v=%{version}; echo ${v:0:3})
Release: 3%{?dist}
License: ASL 2.0
URL: https://www.ovirt.org/
Source: https://resources.ovirt.org/pub/ovirt-%{major_version}/src/%{name}/%{srcname}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: libxml2-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%global _description\
This package contains the Python SDK for version 4 of the oVirt Engine\
API.

%description %_description

%package -n python3-ovirt-engine-sdk4
Summary: %summary
%{?python_provide:%python_provide python3-ovirt-engine-sdk4}

%description -n python3-ovirt-engine-sdk4 %_description

%prep
%autosetup -n %{srcname}-%{version}
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" examples
chmod 0644 examples/*

%build
%py3_build

%install
%py3_install

%files -n python3-ovirt-engine-sdk4
%doc README.adoc
%doc examples
%license LICENSE.txt
%{python3_sitearch}/ovirtsdk4
%{python3_sitearch}/ovirt_engine_sdk_python-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.2-3
- Rebuilt for Python 3.9

* Fri May 08 2020 Juan Orti Alcaine <jortialc@redhat.com> - 4.3.2-2
- Correct provides
- Include python3_sitearch dirs explicitly
- Correct shebang and remove execution of example scripts
- BR: python3-setuptools

* Wed May 06 2020 Juan Orti Alcaine <jortialc@redhat.com> - 4.3.2-1
- Version 4.3.2
- Spec improvements

* Thu Jun 06 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.1-1
- 4.3.1
- Adhere to Fedora packaging guidelines naming schema

* Wed Jun 14 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0-1
- 4.2.0
