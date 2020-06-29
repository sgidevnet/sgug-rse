%global srcname click-plugins
%global srcname_no_dash click_plugins

Name:           python-%{srcname}
Version:        1.1.1
Release:        6%{?dist}
Summary:        Click extension to register CLI commands via setuptools
%global _description \
An extension module for click to register external CLI commands via setuptools \
entry-points.

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-click >= 4.0
BuildRequires:  python3-pytest

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
export LANG=C.UTF-8
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    py.test-%{python3_version} -ra


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname_no_dash}
%{python3_sitelib}/%{srcname_no_dash}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.4-2
- Drop Python 2 subpackage

* Fri Sep 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.4-1
- Update to latest version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.3-3
- Simplify spec with more macros.

* Sun Jul 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.3-2
- Simplify spec a bit.

* Sat Mar 04 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.0.3-1
- Initial package release.
