%global srcname pylons-sphinx-themes
%global desc This is a Python package that contains Sphinx themes for Pylons related \
projects.


Name: python-%{srcname}
Version: 1.0.11
Release: 2%{?dist}
BuildArch: noarch

License: BSD
Summary: Sphinx themes for projects under the Pylons Project
URL: https://github.com/Pylons/%{srcname}
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: python3-devel


%description
%{desc}


%package -n python3-%{srcname}
Summary: %{summary}

%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/pylons_sphinx_themes
%{python3_sitelib}/*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.11-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11 (#1794123).
- https://github.com/Pylons/pylons-sphinx-themes/blob/1.0.11/CHANGES.txt

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.6-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.6-1
- Initial release
