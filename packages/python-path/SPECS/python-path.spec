%global pypi_name path.py

Name:           python-path
Version:        11.5.0
Release:        4%{?dist}
Summary:        Python module wrapper for os.path

License:        MIT
URL:            https://pypi.python.org/pypi/path.py
Source0:        %pypi_source
BuildArch:      noarch

%description
path.py implements path objects as first-class entities, allowing common
operations on files to be invoked on those path objects directly.


%package    -n python3-path
Summary:        Python 3 module wrapper for os.path
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-packaging
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-path}
%description -n python3-path
path.py implements path objects as first-class entities, allowing common
operations on files to be invoked on those path objects directly.


%prep
%autosetup -n %{pypi_name}-%{version} -p1
sed -i 's/\[pytest\]/\[tool:pytest\]/' setup.cfg
sed -i 's/ --flake8//' pytest.ini

# We do not have https://pypi.org/project/importlib-metadata/ in python2
# to populate __version__, so we do it statically here:
sed -i "s/__version__ = 'unknown'/__version__ = '%{version}'/" path.py
sed -i "/importlib_metadata/d" setup.py


%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v


%files -n python3-path
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/path.py
%{python3_sitelib}/path.py-%{version}-py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/test_path.py


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 11.5.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 11.5.0-2
- Subpackage python2-path has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Aug 20 2019 Ken Dreyer <kdreyer@redhat.com> - 11.5.0-1
- Update to latest upstream release (rhbz#1206250)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 5.2-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2-15
- Drop explicit locale setting for python3, use C.UTF-8 for python2
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 5.2-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 5.2-11
- Update conditional

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Thomas Spura <tomspur@fedoraproject.org> - 5.2-8
- rename python-* to python2-*
- expand %%files
- use py_build/install macros

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.2-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Orion Poplawski <orion@cora.nwra.com> - 5.2-4
- Fix py.test call for python3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep  3 2014 Thomas Spura <tomspur@fedoraproject.org> - 5.2-2
- enable testsuite

* Wed Sep  3 2014 Thomas Spura <tomspur@fedoraproject.org> - 5.2-1
- update to 5.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Apr 04 2014 Xavier Lamien <laxathom@fedoraproject.org> - 5.1-1
- Upstream release.
- Add python3's subpackage.

* Fri Jul 26 2013 Xavier Lamien <laxathom@fedoraproject.org> - 4.3-1
- Upstream release.

* Wed Apr 10 2013 Xavier Lamien <laxathom@fedoraproject.org> - 3.0.1-2
- Add %%check stage.
- Update BuildRequire.
- Add missing %%docs.

* Wed Apr 10 2013 Xavier Lamien <laxathom@fedoraproject.org> - 3.0.1-1
- Initial RPM release.
