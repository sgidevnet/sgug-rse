%global modname venusian

Name:           python-%{modname}
Version:        1.2.0
Release:        7%{?dist}
Summary:        A library for deferring decorator actions

License:        BSD
URL:            https://pypi.python.org/pypi/venusian
Source0:        https://pypi.python.org/packages/source/v/venusian/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%global _description\
Venusian is a library which allows framework authors to defer decorator\
actions.  Instead of taking actions when a function (or class) decorator is\
executed at import time, you can defer the action usually taken by the\
decorator until a separate "scan" phase.\


%description %_description

%package -n python3-venusian
Summary:        A library for deferring decorator actions
%{?python_provide:%python_provide python3-venusian}

%description -n python3-venusian
Venusian is a library which allows framework authors to defer decorator
actions.  Instead of taking actions when a function (or class) decorator is
executed at import time, you can defer the action usually taken by the
decorator until a separate "scan" phase.

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg info if it exists
rm -rf %{modname}.egg-info


%build
%py3_build


%install
%py3_install


%check
py.test-3


%files -n python3-venusian
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*.egg-info


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Subpackage python2-venusian has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0.
- https://github.com/Pylons/venusian/blob/1.2.0/CHANGES.rst

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.24.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.0-0.23.a7
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-0.21.a7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-0.19.a7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
