%global srcname pyramid_sawing
%global desc A Pyramid framework plugin for configuring logging via YAML. This uses\
the Python standard-library's logging (initialized using\
logging.config.dictConfig).


Name: python-%{srcname}
Version: 1.1.3
Release: 6%{?dist}
BuildArch: noarch

Summary: Pyramid plugin for YAML logging configuration
License: AGPLv3
URL:     https://github.com/openstax/pyramid_sawing
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/openstax/pyramid_sawing/pull/3
Patch0:  0000-Use-yaml.safe_load-instead-of-load.patch

BuildRequires: python3-devel
BuildRequires: python3-pyramid
BuildRequires: python3-pyyaml


%description
%{desc}


%package -n python3-%{srcname}
Summary: %{summary}

%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGES.rst
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.3-1
- Initial release.
