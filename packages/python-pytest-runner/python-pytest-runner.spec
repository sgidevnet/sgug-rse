%global modulename pytest-runner
%global _modulename pytest_runner

Name:           python-%{modulename}
Version:        4.0
Release:        5%{?dist}
Summary:        Invoke py.test as distutils command with dependency resolution

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-runner
# setuptools-scm requires a pypi tarball and doesn't like github tarball
Source0:        https://files.pythonhosted.org/packages/source/p/%{modulename}/%{modulename}-%{version}.tar.gz

BuildArch: noarch

%global _description \
Setup scripts can use pytest-runner to add setup.py test support for pytest runner.

%description %{_description}

%package -n python2-%{modulename}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modulename}}
Requires:       python2-pytest
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-pytest

%description -n python2-%{modulename} %{_description}

Python 2 version.

%package -n python3-%{modulename}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modulename}}
Requires:       python3-pytest
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest

%description -n python3-%{modulename} %{_description}

Python 3 version.

%prep
%autosetup -n %{modulename}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{modulename}
%doc README.rst
%license LICENSE
%{python2_sitelib}/ptr.py*
%{python2_sitelib}/%{_modulename}-%{version}-py%{python2_version}.egg-info/

%files -n python3-%{modulename}
%doc README.rst
%license LICENSE
%{python3_sitelib}/ptr.py
%{python3_sitelib}/%{_modulename}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/__pycache__/ptr.*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0-2
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Vadim Rutkovsky <vrutkovs@redhat.com> - 4.0-1
- Update to 4.0 (#1544167)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0-2
- Fix broken dep

* Thu Nov 02 2017 Vadim Rutkovsky  <vrutkovs@redhat.com> - 3.0-1
- Update to 3.0 (#1508216)

* Fri Oct 13 2017 Vadim Rutkovsky <vrutkovs@redhat.com> - 2.12.1-1
-  Update to 2.12.1 (#1487972)

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 2.9-6
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 9 2017 Orion Poplawski <orion@cora.nwra.com> - 2.9-4
- Build python 3 version for EPEL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 2.9-2
- Rebuild for Python 3.6

* Sat Aug 06 2016 Vadim Rutkovsky <vrutkovs@redhat.com> - 2.9-1
- Initial package
