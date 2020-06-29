%global pypi_name couchbase

Name: python-%{pypi_name}
Version: 2.5.5
Release: 7%{?dist}
Summary: Python client for Couchbase server
License: ASL 2.0
URL: https://developer.couchbase.com/server/other-products/release-notes-archives/python-sdk
Source0: https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch5: %{name}-0005-do-not-install-tests-as-packages.patch
Patch6: %{name}-0006-remove-typing-package-from-setup.py.patch

BuildRequires: gcc
BuildRequires: libcouchbase-devel

BuildRequires: python3-devel
BuildRequires: python3-testresources >= 0.2.7
BuildRequires: python3-pbr
BuildRequires: python3-twisted
BuildRequires: python3-gevent
BuildRequires: python3-jsonschema
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-numpydoc
BuildRequires: python3-pip

%description
The Couchbase Python SDK allows Python applications to access a Couchbase
cluster. The Python SDK offers a traditional synchronous API as well as
integration with twisted, gevent, and asyncio.

%package -n python3-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The Couchbase Python SDK allows Python applications to access a Couchbase
cluster. The Python SDK offers a traditional synchronous API as well as
integration with twisted, gevent, and asyncio.

%package -n python-%{pypi_name}-doc
Summary: Documentation for Couchbase python client
%description -n python-%{pypi_name}-doc
Documentation for Couchbase python client.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

rm -rf %{python3_sitearch}/%{pypi_name}/tests
rm -rf %{python3_sitearch}/acouchbase/tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/gcouchbase
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/acouchbase
%{python3_sitearch}/txcouchbase
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc README.rst html examples

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.5-7
- Rebuilt for Python 3.9

* Sun May 03 2020 Avram Lubkin <aviso@rockhopper.net> - 2.5.5-6
- Remove python3-configparser as a build requirement

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.5.5-1
- Update to 2.5.5

* Mon Feb 11 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.5.4-1
- Update to 2.5.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.5.3-1
- Update to 2.5.3

* Wed Dec 05 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.5.2-1
- Update to 2.5.2

* Sat Nov 10 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.5.1-2
- Add missing dependency python3-pip

* Thu Nov 08 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Wed Oct 03 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.5.0-1
- Update to 2.5.0

* Tue Oct 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.4.2-2
- Remove python2 package (BZ#1634976)
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Sep 07 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.3.5-3
- Patch for renaming 'async' package to 'asynchronous' for python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.5-2
- Rebuilt for Python 3.7

* Tue May 01 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.3.5-1
- Update to 2.3.5

* Wed Mar 07 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.3.4-2
- Added gcc as build requirement

* Mon Mar 05 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.3.4-1
- Initial package
