%global srcname azure-sdk
%global common_description This project provides a set of Python packages that make it easy to access\
Management (Virtual Machines, ...) or Runtime (ServiceBus using HTTP, Batch,\
Monitor) components of Microsoft Azure Complete feature list of this repo and\
where to find Python packages not in this repo can be found on our Azure SDK for\
Python documentation.

%global _with_tests 0
%global _with_doc 1

%global azure_storage_min_version 1.0.0
%global msrest_min_version 0.4.26
%global msrestazure_min_version 0.5.0

Name:           python-%{srcname}
Version:        4.0.0
Release:        12%{?dist}
Summary:        Microsoft Azure SDK for Python

# All packages are licensed under the MIT license, except:
# - azure-servicebus
# - azure-servicemanagement-legacy
License:        MIT and ASL 2.0
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        %{url}/archive/azure_%{version}/%{srcname}-%{version}.tar.gz
# Install namespace package modules (disabled by default, may be required by
# modules depending on Azure SDK for development)
Patch0:         %{name}-4.0.0-nspkgs.patch
# Disable tests requiring online access to Azure
Patch1:         %{name}-4.0.0-tests.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?_with_tests}
BuildRequires:  python3-azure-devtools
BuildRequires:  python3-azure-storage >= %{azure_storage_min_version}
BuildRequires:  python3-msrest >= %{msrest_min_version}
BuildRequires:  python3-msrestazure >= %{msrestazure_min_version}
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-requests
%endif
%if 0%{?_with_doc}
BuildRequires:  python3-recommonmark
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif
BuildArch:      noarch

%description
%{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}


%if 0%{?_with_doc}
%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.
%endif


%prep
%autosetup -p0 -n %{srcname}-for-python-azure_%{version}%{?prerelease}


%build
%py3_build

%if 0%{?_with_doc}
%make_build -C doc/ html SPHINXBUILD=sphinx-build-3
rm doc/_build/html/.buildinfo
%endif


%install
%py3_install


%check
%if 0%{_with_tests}
PYTHONPATH=
for d in azure-*/; do
    PYTHONPATH+="$d:"
done
export PYTHONPATH=${PYTHONPATH%:}
py.test-%{python3_version}
%endif


%files -n python3-%{srcname}
%doc CONTRIBUTING.md README.rst
%license LICENSE.txt
%{python3_sitelib}/azure/
%{python3_sitelib}/azure_*.egg-info/


%if 0%{?_with_doc}
%files doc
%doc doc/_build/html/
%license LICENSE.txt
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-12
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-9
- Re-enable tests

* Wed Aug 28 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-8
- Disable tests to rebuild package without python-azure-storage (for Python 3.8
  rebuild)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-5
- Enable Python generators
- Enable tests
- Spec cleanup

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-3
- Build documentation with Python 3 on Fedora
- Fix Python 3-only file deployment
- Don't glob everything under the Python sitelib directory

* Mon Aug 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-2
- Delete all Python 3-only files from the python2 subpackage

* Mon Aug 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0
