%global srcname colorclass
%global sum Yet another ANSI color text library for Python

Name:           python-%{srcname}
Version:        2.2.0
Release:        11%{?dist}
Summary:        Yet another ANSI color text library for Python

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz

Source1:        https://github.com/Robpol86/colorclass/blob/master/LICENSE

BuildArch:      noarch

%description
Colorful worry-free console applications for Linux, Mac OS X, and Windows.
Yet another ANSI color text library for Python. Provides "auto colors" for
dark/light terminals. Works on Linux, OS X, and Windows.

%package -n python3-%{srcname}
Summary:        Yet another ANSI color text library for Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Colorful worry-free console applications for Linux, Mac OS X, and Windows.
Yet another ANSI color text library for Python. Provides "auto colors" for
dark/light terminals. Works on Linux, OS X, and Windows.

%prep
%autosetup -n %{srcname}-%{version}
cp %{SOURCE1} .
rm -rf colorclass.egg-info

%build
%py3_build

%install
%py3_install

%check

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colorclass*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-9
- Subpackage python2-colorclass has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 René Ribaud <rene.ribaud@free.fr> - 2.2.0-1
- Include proposed changes by bug #1490059
- Update colorclass to revision 2.2.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 11 2015 René Ribaud <rene.ribaud@free.fr> - 1.2.0-3
- Include changes from Julien's review #2 (Bugzilla #1258405)

* Tue Sep 08 2015 René Ribaud <rene.ribaud@free.fr> - 1.2.0-2
- Include changes from Julien's review (Bugzilla #1258405)

* Mon Aug 31 2015 René Ribaud <rene.ribaud@free.fr> - 1.2.0-1
- Initial rpm
