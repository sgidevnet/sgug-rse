%global mod_name webassets

Name:           python-webassets
Version:        0.12.1
Release:        15%{?dist}
Summary:        Media asset management for python
License:        BSD
URL:            http://github.com/miracle2k/%{mod_name}
Source0:        https://files.pythonhosted.org/packages/source/w/%{mod_name}/%{mod_name}-%{version}.tar.gz
# XXX to be filed
Patch1:         0001-fix-compass-tests-for-Sass-3.4.patch
Patch2:         0002-fix-pyscss-tests.patch
Patch3:         0003-skip-autoprefixer-tests-if-postcss-command-is-not-fo.patch
Patch4:         0004-skip-babel-tests-if-babel-command-is-not-found.patch
Patch5:         0005-fix-rjsmin-test.patch
# https://github.com/miracle2k/webassets/pull/529
# Fix tests with Python 3.9
Patch6:         529.patch
BuildArch:      noarch
%ifarch %{nodejs_arches}
# v8 is just for jsmin.py
BuildRequires:  v8
%endif
BuildRequires:  /usr/bin/sass
# rubygem-compass is broken/retired in Fedora, although webassets still supports it
#BuildRequires:  /usr/bin/compass
BuildRequires:  /usr/bin/uglifyjs
BuildRequires:  /usr/bin/lessc
BuildRequires:  /usr/bin/coffee
BuildRequires:  /usr/bin/handlebars
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# test requirements
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-pillow
# slimit is retired in Fedora, although webassets still supports it
#BuildRequires:  python3-slimit
BuildRequires:  python3-cssutils
BuildRequires:  python3-scss
# this is not ported to Python 3 yet
#BuildRequires:  python3-cssmin
BuildRequires:  python3-rjsmin


%description
Merges, minifies and compresses Javascript and CSS files, 
supporting a variety of different filters, including YUI, 
jsmin, jspacker or CSS tidy. Also supports URL rewriting in CSS files.

%package -n python3-webassets
%{?python_provide:%python_provide python3-%{mod_name}}
Summary:        %{summary}
Requires:       python3-setuptools
Conflicts:      python2-webassets < 0.12.1-9

%description -n python3-webassets
Merges, minifies and compresses Javascript and CSS files, 
supporting a variety of different filters, including YUI, 
jsmin, jspacker or CSS tidy. Also supports URL rewriting in CSS files.


%prep
%setup -q -n %{mod_name}-%{version}
sed -i "s|\r||g" README.rst
sed -i "s|\r||g" docs/index.rst
sed -i "s|\r||g" docs/conf.py
sed -i "s|\r||g" docs/builtin_filters.rst
sed -i "s|\r||g" docs/Makefile
sed -i "s|\r||g" docs/make.bat
sed -i "s|\r||g" docs/faq.rst
# unbundle rjsmin (it's packaged in Fedora)
rm src/webassets/filter/rjsmin/rjsmin.py
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%py3_build

%check
export PYTHONPATH=src
py.test-3

%install
%py3_install

%files -n python3-webassets
%license LICENSE
%doc docs/ README.rst CHANGES PKG-INFO
%{_bindir}/%{mod_name}
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{mod_name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-9
- Subpackage python2-webassets has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.12.1-8
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Jul 16 2018 Dan Callaghan <dcallagh@redhat.com> - 0.12.1-7
- remove requirement on rubygem-compass, which has long been broken in Fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.12.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 03 2017 Dan Callaghan <dcallagh@redhat.com> - 0.12.1-1
- new upstream bug fix release 0.12.1:
  https://github.com/miracle2k/webassets/blob/0.12.1/CHANGES

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuild for Python 3.6

* Fri Oct 07 2016 Dan Callaghan <dcallagh@redhat.com> - 0.12.0-1
- new upstream release 0.12.0:
  https://github.com/miracle2k/webassets/blob/0.12/CHANGES
- removed bundled rjsmin

* Fri Jul 22 2016 Dan Callaghan <dcallagh@redhat.com> - 0.11.1-2
- skip jsmin tests if we are building on an arch which lacks v8
- go back to skipping slimit tests since python-slimit has been retired

* Thu Jul 21 2016 Dan Callaghan <dcallagh@redhat.com> - 0.11.1-1
- new upstream release 0.11.1:
  https://github.com/miracle2k/webassets/blob/0.11.1/CHANGES
- enabled more tests for filters which are now usable in Rawhide
- updated to latest Fedora Python guidelines, use %%license

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 17 2014 Dan Callaghan <dcallagh@redhat.com> - 0.10.1-2
- fixed jsmin filter to work with jsmin.py from v8
- unit tests are run in %%check
- fixed tests to work with Sass 3.4

* Mon Nov 10 2014 Dan Callaghan <dcallagh@redhat.com> - 0.10.1-1
- new upstream release 0.10.1:
  http://webassets.readthedocs.org/en/latest/upgrading.html#in-0-10

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Nov 14 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.9-1
- Updated to new source and added python3 support 

* Tue Sep 24 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8-3
- Added python-setuptools as requires. 

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 1 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8-1
- New Release 

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug  8 2012 Tom Callaway <spot@fedoraproject.org> - 0.7.1-1
- 0.7.1 (cleaned out jsmin.py)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-1
- New release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.5-1
- Initial RPM release
