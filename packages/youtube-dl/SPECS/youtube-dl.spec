%if 0%{?rhel} && 0%{?rhel} < 7
%bcond_with python3
%else
%bcond_without python3
%endif

%if ! %{with python3}
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?__python2: %global __python2 /usr/bin/python2}
%endif

Name:           youtube-dl
Version:        2019.09.12.1
Release:        1%{?dist}
Summary:        A small command-line program to download online videos
License:        Unlicense
URL:            https://yt-dl.org
Source0:        https://github.com/rg3/youtube-dl/releases/download/%{version}/youtube-dl-%{version}.tar.gz
Source1:        https://github.com/rg3/youtube-dl/releases/download/%{version}/youtube-dl-%{version}.tar.gz.sig
# 2016-06-09:
# Merged GPG keys from https://rg3.github.io/youtube-dl/download.html in one file
# gpg --export  --export-options export-minimal "428D F5D6 3EF0 7494 BB45 5AC0 EBF0 1804 BCF0 5F6B" \
# "ED7F 5BF4 6B3B BED8 1C87 368E 2C39 3E0F 18A9 236D" \
# "7D33 D762 FD6C 3513 0481 347F DB4B 54CB A482 6A18" > youtube-dl-gpgkeys.gpg
Source2:        youtube-dl-gpgkeys.gpg
Source3:        %{name}.conf
%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-setuptools
%else
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:  python2-setuptools
%endif
# Tests failed because of no connection in Koji.
# BuildRequires:  python-nose
BuildArch:      noarch
# For source verification with gpgv
BuildRequires:  gnupg2


%description
Small command-line program to download videos from YouTube and other sites.


%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -qn %{name}

# remove pre-built file
rm youtube-dl

cp -a setup.py setup.py.installpath
# Remove files that are installed to the wrong path
sed -i '/youtube-dl.bash-completion/d' setup.py
sed -i '/youtube-dl.fish/d' setup.py
sed -i '/README.txt/d' setup.py

# Remove interpreter shebang from module files.
find youtube_dl -type f -exec sed -i -e '1{/^\#!\/usr\/bin\/env python$/d;};' {} +

%build
%if %{with python3}
%py3_build
%else
%py2_build
%endif


%install
%if %{with python3}
%py3_install
%else
%py2_install
%endif

mkdir -p %{buildroot}%{_sysconfdir}
install -pm644 %{S:3} %{buildroot}%{_sysconfdir}
%if 0%{?fedora}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -pm644 youtube-dl.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/youtube-dl
%else
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -pm644 youtube-dl.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/youtube-dl
%endif
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -pm644 youtube-dl.zsh %{buildroot}%{_datadir}/zsh/site-functions/_youtube-dl
mkdir -p %{buildroot}%{_datadir}/fish/vendor_functions.d
install -pm644 youtube-dl.fish %{buildroot}%{_datadir}/fish/vendor_functions.d/youtube-dl.fish

%check
# This basically cannot work without massive .flake8rc
# starts with flake8 and of course no contributors bothered to make
# their code truly PEP8 compliant.
#
# make offlinetest


%files
%doc AUTHORS ChangeLog README.md
%if %{with python3}
%{python3_sitelib}/youtube_dl/
%{python3_sitelib}/youtube_dl*.egg-info
%else
%{python2_sitelib}/youtube_dl/
%{python2_sitelib}/youtube_dl*.egg-info
%endif
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%if 0%{?fedora}
%{_datadir}/bash-completion/completions/%{name}
%else
%{_sysconfdir}/bash_completion.d/%{name}
%endif
%{_datadir}/zsh/site-functions/_youtube-dl
%{_datadir}/fish/vendor_functions.d/youtube-dl.fish

%changelog
* Wed Sep 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2019.09.12.1-1
- Update to 2019.09.12.1

* Wed Sep 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2019.09.12-2
- Add Fish shell completion

* Wed Sep 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2019.09.12-1
- Update to 2019.09.12

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.07.30-2
- Rebuilt for Python 3.8

* Tue Jul 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 2019.07.30-1
- 2019.07.30

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.06.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Till Maas <opensource@till.name> - 2019.06.21-1
- Update to new upstream release with important bugfixes

* Sun Jun 16 2019 Michael Cronenworth <mike@cchtml.com> - 2019.06.08-1
- Update to 2019.06.08

* Wed Apr 24 2019 Till Maas <opensource@till.name> - 2019.04.24-1
- Update to new upstream release with important bugfixes

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Till Maas <opensource@till.name> - 2019.01.30-1
- Update to 2019.01.30

* Thu Jan 24 2019 Richard Shaw <hobbes1069@gmail.com> - 2019.01.24-1
- Update to 2019.01.24.

* Thu Dec 27 2018 Matěj Cepl <mcepl@cepl.eu> - 2018.12.17-1
- Update to the latest upstream release.
- Make python-setuptools Required.

* Sat Dec 15 2018 Matěj Cepl <mcepl@cepl.eu> - 2018.12.09-1
- Update to the latest upstream release.

* Sun Sep 30 2018 Matěj Cepl <mcepl@cepl.eu> - 2018.09.26-1
- Update to the latest upstream release.

* Sat Sep 08 2018 Matěj Cepl <mcepl@suse.com> - 2018.09.08-1
- Update to the latest upstream release.

* Sat Aug 18 2018 Matěj Cepl <mcepl@suse.com> - 2018.08.04-1
- Update to the latest release.

* Mon Jul 23 2018 Matěj Cepl <mcepl@redhat.com> - 2018.07.21-2
- Add youtube-dl-2018.07.21-ceskatelevize-https.patch to workaround
  (badly) around https://github.com/rg3/youtube-dl/issues/16307

* Sat Jul 21 2018 Matěj Cepl <mcepl@redhat.com> - 2018.07.21-1
- Update to the latest release.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.05.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.05.18-2
- Rebuilt for Python 3.7

* Fri May 25 2018 Matěj Cepl <mcepl@redhat.com> - 2018.05.18-1
- Update to the latest release.

* Tue Apr 24 2018 Matěj Cepl <mcepl@redhat.com> - 2018.04.16-1
- Update to the latest release.

* Mon Mar 26 2018 Matěj Cepl <mcepl@redhat.com> - 2018.03.26.1-1
- Use Python 3 for EPEL-7.

* Wed Mar 14 2018 Matěj Cepl <mcepl@redhat.com> - 2018.03.10-1
- Update to the latest release.

* Tue Feb 27 2018 Matěj Cepl <mcepl@redhat.com> - 2018.02.26-1
- Update to the latest release.

* Fri Feb 09 2018 Matěj Cepl <mcepl@redhat.com> - 2018.02.08-2
- Remove hardcoded-library-path (#1539993)

* Fri Feb 09 2018 Matěj Cepl <mcepl@redhat.com> - 2018.02.08-1
- Update to the latest release.

* Tue Jan 23 2018 Matěj Cepl <mcepl@redhat.com> - 2018.01.21-1
- Update to the latest release.

* Thu Dec 28 2017 Matěj Cepl <mcepl@redhat.com> - 2017.12.23-1
- Update to latest release

* Wed Dec 13 2017 Matěj Cepl <mcepl@redhat.com> - 2017.12.10-1
- Update to latest release

* Sat Nov 25 2017 Matěj Cepl <mcepl@redhat.com> - 2017.11.15-1
- Update to latest release

* Tue Nov 07 2017 Matěj Cepl <mcepl@redhat.com> - 2017.11.06-1
- Update to latest release

* Thu Oct 19 2017 Matěj Cepl <mcepl@redhat.com> - 2017.10.15.1-1
- Update to latest release

* Mon Oct 02 2017 Till Maas <opensource@till.name> - 2017.10.01-1
- Update to latest release

* Sat Sep 23 2017 Matěj Cepl <mcepl@redhat.com> - 2017.09.15-1
- Update to latest release.

* Sat Sep 02 2017 Matěj Cepl <mcepl@redhat.com> - 2017.09.02-1
- Update to latest release.

* Thu Aug 31 2017 Till Maas <opensource@till.name> - 2017.08.23-2
- Manually follow redirect for source URLs to please rpmlint (#1414964)

* Fri Aug 25 2017 Matěj Cepl <mcepl@redhat.com> - 2017.08.23-1
- Update to latest release.

* Wed Aug 16 2017 Matěj Cepl <mcepl@redhat.com> - 2017.08.13-1
- Update to latest release.

* Sat Jul 29 2017 Matěj Cepl <mcepl@redhat.com> - 2017.07.23-1
- Update to latest release.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.07.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Matěj Cepl <mcepl@redhat.com> - 2017.07.09-1
- Update to latest release.

* Wed Jun 28 2017 Matěj Cepl <mcepl@redhat.com> - 2017.06.25-1
- Update to latest release.

* Sat Jun 03 2017 Matěj Cepl <mcepl@redhat.com> - 2017.05.29-1
- Update to latest release.

* Thu May 18 2017 Matěj Cepl <mcepl@redhat.com> - 2017.05.18.1-1
- Update to latest release.

* Thu May 18 2017 Gwyn Ciesla <limburgher@gmail.com> - 2017.05.14-1
- Update to latest release.

* Mon May 08 2017 Matěj Cepl <mcepl@redhat.com> - 2017.05.07-1
- Update to the latest release.

* Tue Apr 25 2017 Matěj Cepl <mcepl@redhat.com> - 2017.04.17-1
- Update to the latest release.

* Mon Apr 10 2017 Matěj Cepl <mcepl@redhat.com> - 2017.04.09-1
- Update to the latest release.

* Thu Mar 23 2017 Matěj Cepl <mcepl@redhat.com> - 2017.03.22-1
- Update to the latest release.

* Thu Feb 16 2017 Matěj Cepl <mcepl@redhat.com> - 2017.02.16-1
- Update to the new release.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.01.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Matěj Cepl <mcepl@redhat.com> - 2017.01.31-1
- Update to the new release.

* Sun Jan 29 2017 Till Maas <opensource@till.name> - 2017.01.28-1
- Update to new release

* Thu Jan 12 2017 Till Maas <opensource@till.name> - 2017.01.10-1
- Update to new release

* Wed Dec 28 2016 Matěj Cepl <mcepl@redhat.com> - 2016.12.22-1
- Update to latest upstream release

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2016.12.09-2
- Rebuild for Python 3.6

* Sun Dec 11 2016 Matěj Cepl <mcepl@redhat.com> - 2016.12.09-1
- Update to latest upstream release

* Fri Nov 25 2016 Matěj Cepl <mcepl@redhat.com> - 2016.11.22-1
- Update to latest upstream release

* Sun Nov 20 2016 Till Maas <opensource@till.name> - 2016.11.18-1
- Update to 2016.11.18

* Tue Oct 25 2016 Till Maas <opensource@till.name> - 2016.10.25-1
- Update to 2016-10-25
- Cleanup changelog
- Remove %%license workaround for EPEL, %%license is now defined in EPEL
- Remove interpreter line from module files
- Move bash completion to new path on Fedora
- Use py_build/py_install macros

* Wed Oct 12 2016 Matěj Cepl <mcepl@redhat.com> - 2016.10.12-1
- Update to latest upstream release

* Sun Sep 18 2016 Till Maas <opensource@till.name> - 2016.09.18-1
- Update to lastest upstream release

* Sat Sep 17 2016 Till Maas <opensource@till.name> - 2016.09.15-1
- Update to latest upstream release

* Tue Aug 30 2016 Matěj Cepl <mcepl@redhat.com> - 2016.08.31-1
- Update to the latest upstream release.

* Wed Jul 20 2016 Matěj Cepl <mcepl@redhat.com> - 2016.07.17-1
- Update to the latest upstream release.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2016.06.25-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jun 26 2016 Matěj Cepl <mcepl@redhat.com> - 2016.06.25-1
- Update to the latest upstream release.

* Thu May 19 2016 Matěj Cepl <mcepl@redhat.com> 2016.05.16-1
- Update to the latest upstream release.
- Update upstream GPG keys

* Wed May  4 2016 Matěj Cepl <mcepl@redhat.com> - 2016.05.01-1
- Update to the latest release.

* Fri Apr 15 2016 Till Maas <opensource@till.name> - 2016.04.13-2
- Fix build deps

* Thu Apr 14 2016 Matěj Cepl <mcepl@redhat.com> 2016.04.13-1
- Update to the latest release.

* Mon Mar 21 2016 Till Maas <opensource@till.name> - 2016.03.06-2
- Use gpgv2 for source verification

* Thu Mar 10 2016 Matěj Cepl <mcepl@redhat.com> - 2016.03.06-1
- Update to latest release.

* Mon Feb 15 2016 Matěj Cepl <mcepl@redhat.com> - 2016.02.13-1
- Update to latest release.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.12.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Matěj Cepl <mcepl@redhat.com> - 2015.12.23-1
- Update to latest release.

* Sun Dec 06 2015 Till Maas <opensource@till.name> - - 2015.12.05-1
- Update to latest release

* Tue Dec 01 2015 Jon Ciesla <limburgher@gmail.com> - 2015.11.27.1-1
- Update to latest release.

* Sun Nov 22 2015 Till Maas <opensource@till.name> - 2015.11.21-1
- Update to new release

* Mon Nov 16 2015 Matěj Cepl <mcepl@redhat.com> - 2015.11.15-1
- Update to new release.

* Sun Nov 15 2015 Till Maas <opensource@till.name> - 2015.11.13-2
- Use python3 on Fedora (#1282086)

* Fri Nov 13 2015 Till Maas <opensource@till.name> - 2015.11.13-1
- Update to new release

* Sun Oct 18 2015 Matěj Cepl <mcepl@redhat.com> - 2015.10.16-1
- Update to the latest release (#1270800)

* Fri Oct 09 2015 Matěj Cepl <mcepl@redhat.com> - 2015.10.09-1
- Update to the latest release (#1265448)

* Sun Sep 20 2015 Matěj Cepl <mcepl@redhat.com> - 2015.09.09-1
- Update to the latest release (#1251785)

* Sat Aug 08 2015 Matej Cepl <mcepl@redhat.com> - 2015.08.06.1-1
- Update to the latest release (#1240646)

* Sat Jul 04 2015 Matej Cepl <mcepl@redhat.com> - 2015.07.04-1
- Update to the latest release (#1231593)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.06.04.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Matej Cepl <mcepl@redhat.com> - 2015.06.04.1-2
- Fix the License: field to Unlicense.

* Fri Jun 05 2015 Matej Cepl <mcepl@redhat.com> - 2015.06.04.1-1
- Update to the latest release (#1222017)

* Fri May 15 2015 Matej Cepl <mcepl@redhat.com> - 2015.05.10-1
- Update to the latest release (#1218015, 1200569, 1206484)

* Wed Apr 29 2015 Matej Cepl <mcepl@redhat.com> - 2015.04.28-1
- Update to the latest release (#1210132)

* Sat Apr 04 2015 Matej Cepl <mcepl@redhat.com> - 2015.04.03-1
- Update to the latest release (#1205700)

* Thu Mar 19 2015 Matej Cepl <mcepl@redhat.com> - 2015.03.18-1
- Update to latest release (# 1201585)

* Thu Mar 05 2015 Matej Cepl <mcepl@redhat.com> - 2015.03.03.1-1
- Update to latest release (# 1195539, 1195779)

* Sun Feb 22 2015 Matej Cepl <mcepl@redhat.com> - 2015.02.21-1
- Update to latest release

* Wed Feb 18 2015 Matej Cepl <mcepl@redhat.com> - 2015.02.18.1-1
- Update to latest release

* Mon Feb 16 2015 Matej Cepl <mcepl@redhat.com> - 2015.02.11-1
- Show must go on!

* Tue Feb 10 2015 Till Maas <opensource@till.name> - 2015.02.10.4-1
- Update to latest release

* Tue Feb 10 2015 Till Maas <opensource@till.name> - 2015.02.10.2-1
- Update to latest release
- remove pre-built file in %%setup

* Sat Jan 31 2015 Till Maas <opensource@till.name> - 2015.01.30.1-1
- Update to new release
- Use %%license

* Tue Jan 27 2015 Till Maas <opensource@till.name> - 2015.01.25-1
- Update to new release

* Tue Jan 27 2015 Alexey Kurov <nucleo@fedoraproject.org> - 2015.01.25.1-1
- Python 2.7 byte compile

* Fri Jan 16 2015 Matej Cepl <mcepl@redhat.com> - 2015.01.15.1-1
- Update to new release.

* Wed Jan 14 2015 Till Maas <opensource@till.name> - 2015.01.11-1
- Update to new release
