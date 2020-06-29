%global srcname hupper
%global sum Integrated process monitor for developing servers

Name:           python-%{srcname}
Version:        1.10.2
Release:        2%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# python3 test buildrequires
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildRequires: python3-mock

%description
hupper is an integrated process monitor that will track changes
to any imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
hupper is an integrated process monitor that will track changes
to any imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest

%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTING.rst docs/ LICENSE.txt PKG-INFO README.rst rtd.txt
%{python3_sitelib}/*
%{_bindir}/hupper

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.2-2
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Kevin Fenzi <kevin@scrye.com> - 1.10.2-1
- Update to 1.10.2. Fixes bug #1804411

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Kevin Fenzi <kevin@scrye.com> - 1.9.1-1
- Update to 1.9.1. Fixes bug #1761667

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 1.8.1-4
- Drop python2 subpackages. Fixes bug #1744653

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.8.1-1
- Update to 1.8.1. Fixes bug #1717277

* Sat Mar 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.6.1-1
- Update to 1.6.1. Fixes bug #1687548

* Sun Mar 10 2019 Kevin Fenzi <kevin@scrye.com> - 1.6-1
- Update to 1.6. Fixes bug #1686273

* Sat Feb 23 2019 Kevin Fenzi <kevin@scrye.com> - 1.5-1
- Update to 1.5. Fixes bug #1677934

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-2
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Kevin Fenzi <kevin@scrye.com> - 1.3-1
- Update to 1.3. Fixes bug #1592948

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.2-1
- Initial version for Fedora. 

