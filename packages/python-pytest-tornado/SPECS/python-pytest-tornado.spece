%global srcname pytest-tornado
%global srcname_ pytest_tornado

Name:           python-%{srcname}
Version:        0.8.0
Release:        6%{?dist}
Summary:        Py.test plugin for testing of asynchronous tornado applications

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/eugeniy/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A py.test plugin providing fixtures and markers to simplify testing of \
asynchronous tornado applications.

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest >= 3.6
BuildRequires:  python3-tornado >= 4.1

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" PYTHONDONTWRITEBYTECODE=1 \
    py.test-%{python3_version}


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname_}
%{python3_sitelib}/%{srcname_}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.0-1
- Update to latest version

* Tue Apr 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-2
- Drop Python 2 subpackage

* Mon Apr 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- Update to latest version

* Sat Apr 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-2
- Remove test bytecode from package

* Mon Apr 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.7

* Sun Apr 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-1
- Update to latest version.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.5-3
- Use version tag instead of unnecessary commit archive.

* Sun Oct 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.5-2
- Simplify spec against latest template.

* Sat Mar 04 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.5-1
- Initial package release.
