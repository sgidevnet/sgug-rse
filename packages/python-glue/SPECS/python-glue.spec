%global srcname glue
%global sum A simple command line tool to generate CSS sprites

Name:           python-%{srcname}
Version:        0.13
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://github.com/jorgebastida/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{srcname}-%{version}.tar.gz
# https://github.com/jorgebastida/glue/pull/211
Patch0:         python-glue.remove-jinja2-version-restriction.patch
# https://github.com/jorgebastida/glue/pull/208
Patch1:         python-glue.python3-support-without-2to3.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-pillow
Requires:       python3-jinja2
Requires:       python3-pillow

%description
Glue is a simple command line tool to generate CSS sprites using any kind
of source images like PNG, JPEG or GIF. Glue will generate a unique PNG file
containing every source image and a CSS file including the necessary CSS
classes to use the sprite.

%package -n %{srcname}
Summary:        %{sum}
Provides:       python-%{srcname} = %{version}-%{release}
Obsoletes:      python-%{srcname} < 0.11.1-6

%description -n %{srcname}
Glue is a simple command line tool to generate CSS sprites using any kind
of source images like PNG, JPEG or GIF. Glue will generate a unique PNG file
containing every source image and a CSS file including the necessary CSS
classes to use the sprite.

%prep
%autosetup -n %{srcname}-%{version} -p 1
# See https://github.com/jorgebastida/glue/pull/212
rm docs/.gitignore
rm -rf glue.egg-info
# Remove the shebang that set the python executable since that's
# generated later
sed -i -e "1d" glue/bin.py

%build
%{__python3} setup.py build egg_info build_sphinx # build_sphinx needs egg_info
rm build/sphinx/html/.buildinfo

%install
%py3_install

%files -n %{srcname}
%license COPYING
%doc AUTHORS build/sphinx/html
%{python3_sitelib}/*
%{_bindir}/%{srcname}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.13-1
- Update to 0.13 (#1447657)

* Tue Feb 18 2020 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.12-1
- Update to 0.12 (#1447657)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.11.1-10
- Add missing build dependency

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu May 26 2016 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.11.1-7
- Fixed Source0 to point to new PyPi predictable URL format

* Sun May 15 2016 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.11.1-6
- Add subpackage glue, which uses python3 and obsoletes python-glue

* Tue May 10 2016 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.11.1-5
- Fix crash when using Jinja2 2.8
- Remove docs/.gitignore which is include in the source distribution by mistake
- Fix some rpm lint warnings

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.11.1-2
- Build and install HTML docs instead of doc sources, mark COPYING as %%license

* Sat Apr 25 2015 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.11.1-1
- Update upstream version to 0.11.1
* Sun Mar 15 2015 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.9.4-1
- Update upstream version to 0.9.4
- Removed the patch since my changes were accepted upstream so the patch
  is not needed anymore.
* Wed Mar 04 2015 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.9.2-1
- Update upstream version to 0.9.2
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.9.1-1
- Update upstream version to 0.9.1
- Added check step for running the package tests
* Tue Feb 11 2014 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.4.1-1
- Update upstream version to 0.4.1
* Wed Dec 4 2013 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.4-1
- Update upstream version to 0.4
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Wed Feb 6 2013 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.3-1
- Update upstream version to 0.3
* Sat Dec 15 2012 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.2.9-1
- Update upstream version to 0.2.9
- Update the patch to remove the Pillow dependency
- Use version macro in the Source0 to avoid repetition
* Wed Oct 31 2012 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.2.8.1-1
- Update upstream version to 0.2.8.1
* Tue Oct 23 2012 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.2.7-2
- Remove the shebang part of the glue.py script
- Remove the glue.egg-info directory in the prep section
- Remove the 'rm -rf $RPM_BUILD_ROOT' in the install section
* Mon Oct 22 2012 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com> - 0.2.7-1
- New package.
