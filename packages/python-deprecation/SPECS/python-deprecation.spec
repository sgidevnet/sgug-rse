%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name deprecation

Name:           python-%{pypi_name}
Version:        2.0.6
Release:        7%{?dist}
Summary:        A library to handle automated deprecations
License:        ASL 2.0
URL:            http://deprecation.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        A library to handle automated deprecations
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests.
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        A library to handle automated deprecations
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
The deprecation library provides a deprecated decorator and a
fail_if_not_removed decorator for your tests.
%endif


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python3}
%py3_install
%endif
%if %{with python2}
%py2_install
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 01 2019 Javier Peña <jpena@redhat.com> - 2.0.6-2
- Removed python2 subpackage from Fedora (rhbz#1694620)

* Wed Feb 06 2019 Alfredo Moralejo <amoralej@redhat.com> - 2.0.6-1
- Update to 2.0.6.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-9
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Javier Peña <jpena@redhat.com> - 1.0-3
- Fix description for subpackages

* Tue Feb 28 2017 Javier Peña <jpena@redhat.com> - 1.0-2
- Added license file from git repo

* Wed Feb 15 2017 Javier Peña <jpena@redhat.com> - 1.0-1
- Initial package.
