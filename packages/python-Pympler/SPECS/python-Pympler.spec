%global pname Pympler

%global desc \
Pympler is a development tool to measure, monitor and analyze the memory\
behavior of Python objects in a running Python application.\
\
By pympling a Python application, detailed insight in the size and the lifetime\
of Python objects can be obtained. Undesirable or unexpected runtime behavior\
like memory bloat and other “pymples” can easily be identified.\
\
Pympler integrates three previously separate modules into a single,\
comprehensive profiling tool. The asizeof module provides basic size information\
for one or several Python objects, module muppy is used for on-line monitoring\
of a Python application and module Class Tracker provides off-line analysis of\
the lifetime of selected Python objects.

Name: python-%{pname}
Version: 0.8
Release: 4%{?dist}
Summary: Measure, monitor and analyze the memory behavior of Python objects
License: ASL 2.0 and BSD and MIT
# bundled stuff
# pympler/asizeof.py: BSD
# pympler/static/jquery.sparkline.min.js: BSD
# pympler/templates/jquery.flot*.min.js: MIT
URL: http://pythonhosted.org/Pympler/
Source0: https://pypi.python.org/packages/source/P/%{pname}/%{pname}-%{version}.tar.gz
# https://github.com/pympler/pympler/issues/104
Patch0: https://github.com/pympler/pympler/commit/bfc2f957831c96a39acedba25fb0da99c5a37805.diff
# drop python shebang from asizeof.py
Patch2: %{name}-no-shebang.patch
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-bottle
BuildRequires: python3-devel
BuildRequires: python3-matplotlib
BuildRequires: python3-setuptools
Requires: python3-bottle
# http://www.flotcharts.org
Provides: bundled(js-jquery-flot) = 0.8.3
# https://github.com/krzysu/flot.tooltip
Provides: bundled(js-jquery-flot-tooltip) = 0.8.4
# http://omnipotent.net/jquery.sparkline/
Provides: bundled(js-jquery-sparkline) = 2.1.1
# asizeof.py is bundled
Provides: bundled(python%{python3_version}dist(asizeof))
# required by pympler/charts.py, but doesn't throw an exception without
Recommends: python3-matplotlib
# pympler/panels.py is an extension for django-debug-toolbar
Enhances: python3-django-debug-toolbar

%description -n python3-%{pname}
%{desc}

%prep
%setup -q -n %{pname}-%{version}
rm pympler/util/bottle.py
chmod -x pympler/asizeof.py
%patch0 -p1
%patch2 -p1 -b .no-shebang

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%files -n python3-%{pname}
%license LICENSE
%doc NOTICE README.md
%{python3_sitelib}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/pympler

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuilt for Python 3.9

* Sat May 02 2020 Dominik Mierzejewski <rpm@greysector.net> 0.8-3
- fix build with Python 3.9 (#1791963)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Dominik Mierzejewski <rpm@greysector.net> 0.8-1
- update to 0.8 (#1771742)
- re-bundle flot (nodejs-flot was retired)
- re-enable failing test (fixed upstream)

* Thu Sep 12 2019 Dominik Mierzejewski <rpm@greysector.net> 0.7-1
- update to 0.7 (#1696870)
- disable one test failing with Python 3.8
  (https://github.com/pympler/pympler/issues/102)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Dominik Mierzejewski <rpm@greysector.net> 0.6-1
- update to 0.6
- mark asizeof.py as bundled (#1649274)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5-3
- Subpackage python2-Pympler has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Dominik Mierzejewski <rpm@greysector.net> 0.5-1
- update to 0.5
- drop obsolete patches
- use pythonX_version macros in files list

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.3-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 10 2016 Dominik Mierzejewski <rpm@greysector.net> 0.4.3-2
- drop CC-BY-SA-NC from license list and fix typo
- actually unbundle nodejs-flot
- add a weak dep for python{2,3}-django-debug-toolbar
- drop python shebang from asizeof.py

* Mon May 16 2016 Dominik Mierzejewski <rpm@greysector.net> 0.4.3-1
- update to 0.4.3
- build for python3 as well
- unbundle python-bottle

* Sun Aug 09 2015 Dominik Mierzejewski <rpm@greysector.net> 0.4.2-1
- initial build
