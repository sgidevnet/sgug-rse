%global srcname flufl.testing
%global pkgname flufl-testing
%global summary Small collection of test tool plugins
%global _description \
This package contains a small collection of test helpers that Barry Warsaw \
uses in almost all his packages. Specifically, plugins for the following \
test tools are provided:  \
- nose2   \
- flake8  \
Python 3.4 is the minimum supported version.


Name:           python-%{pkgname}
Version:        0.8
Release:        3%{?dist}
Summary:        %{summary}

License:        ASL 2.0
URL:            https://gitlab.com/warsaw/flufl.testing
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-srpm-macros
BuildRequires:  python%{python3_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%endif

%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pkgname}}

%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%py3_install
%if 0%{?with_python3_other}
%py3_other_install
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst NEWS.rst
%{python3_sitelib}/flufl/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}-nspkg.pth

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%doc README.rst NEWS.rst
%{python3_other_sitelib}/flufl/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}.egg-info/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_version}-nspkg.pth
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Aurelien Bompard <abompard@fedoraproject.org> - 0.8-1
- Version 0.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Aurelien Bompard <abompard@fedoraproject.org> - 0.4-5
- Fix BuildRequires name

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4-2
- Rebuild for Python 3.6

* Thu Dec 01 2016 Aurelien Bompard <abompard@fedoraproject.org> - 0.4-1
- Initial package.
