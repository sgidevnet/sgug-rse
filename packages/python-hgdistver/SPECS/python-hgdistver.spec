%global srcname hgdistver
%global sum A Python library to generate package version info from mercurial tags


Name:           python-hgdistver
Version:        0.25
Release:        16%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://bitbucket.org/RonnyPfannschmidt/hgdistver/
Source0:        http://pypi.python.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
hgdistver is a simple drop-in to support setup.py in mercurial based projects.
It's supposed to generate version numbers from mercurial's meta-data. It tries
to use the current tag and falls back to the next reachable tagged ancestor
and using the distance to it as .post marker.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
hgdistver is a simple drop-in to support setup.py in mercurial based projects.
It's supposed to generate version numbers from mercurial's meta-data. It tries
to use the current tag and falls back to the next reachable tagged ancestor
and using the distance to it as .post marker.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CHANGELOG.rst README.rst 
%license LICENSE
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}*.egg-info
%{python3_sitelib}/__pycache__/%{srcname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.25-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25-13
- Rebuilt for Python 3.8

* Sun Aug 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25-12
- Subpackage python2-hgdistver has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.25-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.25-1
- Cleanup
- Update to latest upstream release 0.25

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.21-3
- Activate python3 package

* Fri Oct 03 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.21-2
- Add python3 package

* Sun Sep 14 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.21-1
- Update URL
- Update to new upstream release 0.21

* Fri Sep 12 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.20-1
- Update to new upstream release 0.20

* Wed Sep 03 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.19-1
- Update to new upstream release 0.19

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 01 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.16-2
- Bundled egg-info removed

* Sun Oct 21 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.16-1
- Update to new upstream release 0.16

* Fri Jun 08 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.15-1
- Initial package
