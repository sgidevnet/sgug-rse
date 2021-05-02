Name:           lilypond-doc
Version:        2.19.84
Release:        1%{?dist}
Summary:        HTML documentation for LilyPond

License:        GPLv3
URL:            http://www.lilypond.org
Source0:        http://www.lilypond.org/downloads/binaries/documentation/lilypond-%{version}-1.documentation.tar.bz2
BuildArch:      noarch


%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

This package contains the HTML documentation for LilyPond.


%prep
%setup -q -c


%build
# Remove empty files
rm -f input/mutopia/E.Satie/petite-ouverture-a-danser.png
rm -f input/mutopia/J.S.Bach/wtk1-fugue2.png
rm -f input/mutopia/W.A.Mozart/mozart-hrn-3.png


%install
mkdir -p $RPM_BUILD_ROOT


%files
%license license
%doc share


%changelog
* Fri Feb 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.19.84-1
- 2.19.84

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.83-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.19.83
- 2.19.83

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.19.82-1
- 2.19.82.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.19.81-1
- 2.19.81.
- Minor spec cleanup.

* Mon Oct 16 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.80-1
- 2.19.80.

* Mon Aug 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.65-1
- 2.19.65.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.64-1
- 2.19.64.

* Wed Jun 28 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.63-1
- 2.19.63.

* Wed Jun 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.62-1
- 2.19.62.

* Mon May 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.61-1
- 2.19.61.

* Tue May 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.60-1
- 2.19.60.

* Mon Apr 10 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.59-1
- 2.19.59.

* Wed Mar 29 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.58-1
- 2.19.58.

* Tue Mar 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 2.19.57-1
- 2.19.57.

* Mon Feb 27 2017 Jon Ciesla <limburgher@gmail.com> - 2.19.56-1
- 2.19.56.

* Mon Feb 13 2017 Jon Ciesla <limburgher@gmail.com> - 2.19.55-1
- 2.19.55.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Jon Ciesla <limburgher@gmail.com> - 2.19.54-1
- 2.19.54.

* Mon Dec 19 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.53-1
- 2.19.53.

* Mon Dec 05 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.52-1
- 2.19.52.

* Mon Nov 21 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.51-1
- 2.19.51.

* Mon Nov 07 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.50-1
- 2.19.50.

* Tue Oct 18 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.49-1
- 2.19.49.

* Wed Sep 14 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.48-1
- 2.19.48.

* Wed Aug 31 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.47-1
- 2.19.47.

* Wed Jul 27 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.46-1
- 2.19.46.

* Sun Jul 10 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.45-1
- 2.19.45.

* Wed Jun 22 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.44-1
- 2.19.44.

* Fri Jun 10 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.43-1
- 2.19.43.

* Thu May 19 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.42-1
- 2.19.42.

* Mon May 02 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.41-1
- 2.19.41.

* Mon Apr 18 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.40-1
- 2.19.40.

* Fri Apr 01 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.39-1
- 2.19.39.

* Mon Mar 14 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.38-1
- 2.19.38.

* Mon Feb 29 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.37-1
- 2.19.37.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.36-1
- 2.19.36.

* Mon Jan 04 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.35-1
- 2.19.35.

* Wed Dec 23 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.34-1
- 2.19.34.

* Mon Dec 07 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.33-1
- 2.19.33.

* Tue Nov 24 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.32-1
- 2.19.32.

* Wed Nov 11 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.31-1
- 2.19.31.

* Mon Oct 26 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.30-1
- 2.19.30.

* Tue Oct 20 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.29-1
- 2.19.29.

* Mon Sep 28 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.28-1
- 2.19.28.

* Mon Sep 14 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.27-1
- 2.19.27.
- Fix changelog.

* Mon Aug 31 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.26-1
- 2.19.26.

* Mon Aug 10 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.25-1
- 2.19.25.

* Tue Jul 28 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.24-1
- 2.19.24.

* Tue Jul 21 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.23-1
- 2.19.23.

* Mon Jun 29 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.22-1
- 2.19.22.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.21-1
- 2.19.21.

* Fri May 15 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.20-1
- 2.19.20.

* Tue Apr 28 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.19-1
- 2.19.19.

* Mon Apr 06 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.18-1
- 2.19.18.

* Mon Mar 16 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.17-1
- 2.19.17.

* Sun Mar 01 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.16-1
- 2.19.16.

* Thu Jan 29 2015 Jon Ciesla <limburgher@gmail.com> - 2.19.15-1
- 2.19.15.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Jon Ciesla <limburgher@gmail.com> - 2.18.2-1
- 2.18.2.

* Fri Jan 03 2014 Jon Ciesla <limburgher@gmail.com> - 2.18.0-1
- Update to 2.18.0, BZ 1047196.

* Mon Dec 09 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.97-1
- Update to 2.17.97.

* Mon Nov 25 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.96-1
- Update to 2.17.96.

* Mon Nov 04 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.30-1
- Update to 2.17.30.

* Wed Oct 23 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.29-1
- Update to 2.17.29.

* Mon Sep 09 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.26-1
- Update to 2.17.26.

* Mon Aug 26 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.25-1
- Update to 2.17.25.

* Tue Aug 13 2013 Jon Ciesla <limburgher@gmail.com> - 2.17.24-1
- Update to 2.17.24.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Jon Ciesla <limburgher@gmail.com> - 2.16.2-1
- Update to 2.16.2.

* Sat Nov 10 2012 Jon Ciesla <limburgher@gmail.com> - 2.16.1-1
- Update to 2.16.1.

* Fri Aug 24 2012 Jon Ciesla <limburgher@gmail.com> - 2.16.0-1
- Update to 2.16.0.

* Sun Aug 12 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.95-1
- Update to 2.15.95.

* Sat Aug 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.42-1
- Update to 2.15.42.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.41-1
- Update to 2.15.41.

* Wed Jun 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.40-1
- Update to 2.15.40.

* Wed May 23 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.39-1
- Update to 2.15.39.

* Fri May 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.38-1
- Update to 2.15.38.

* Fri Apr 20 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.37-1
- Update to 2.15.37.

* Mon Apr 09 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.36-1
- Update to 2.15.36.

* Wed Mar 28 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.35-1
- Update to 2.15.35.

* Tue Mar 20 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.34-1
- Update to 2.15.34.

* Fri Mar 09 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.33-1
- Update to 2.15.33.

* Tue Mar 06 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.32-1
- Update to 2.15.32.

* Wed Feb 29 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.31-1
- Update to 2.15.31.

* Sat Feb 18 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.30-1
- Update to 2.15.30.

* Fri Feb 10 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.29-1
- Update to 2.15.29.

* Sat Feb 04 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.28-1
- Update to 2.15.28.

* Wed Jan 25 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.27-1
- Update to 2.15.27.

* Mon Jan 16 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.26-1
- Update to 2.15.26.

* Sun Jan 08 2012 Jon Ciesla <limburgher@gmail.com> - 2.15.24-1
- Update to 2.15.24.

* Wed Dec 28 2011 Jon Ciesla <limburgher@gmail.com> - 2.15.23-1
- Update to 2.15.23.

* Fri Dec 16 2011 Jon Ciesla <limburgher@gmail.com> - 2.15.22-1
- Update to 2.15.22.

* Thu Dec 08 2011 Jon Ciesla <limburgher@gmail.com> - 2.15.21-1
- Update to 2.15.21.

* Mon Nov 28 2011 Jon Ciesla <limb@jcomserv.net> 2.15.20-1
- Update to 2.15.20.

* Tue Nov 22 2011 Jon Ciesla <limb@jcomserv.net> 2.15.19-1
- Update to 2.15.19.

* Sat Nov 12 2011 Jon Ciesla <limb@jcomserv.net> 2.15.18-1
- Update to 2.15.18.

* Fri Oct 28 2011 Jon Ciesla <limb@jcomserv.net> 2.15.16-1
- Update to 2.15.16.

* Fri Oct 21 2011 Jon Ciesla <limb@jcomserv.net> 2.15.14-1
- Update to 2.15.14.

* Thu Jul 28 2011 Jon Ciesla <limb@jcomserv.net> 2.14.2-1
- Update to 2.14.2.

* Mon Jun 13 2011 Jon Ciesla <limb@jcomserv.net> 2.14.1-1
- Update to 2.14.1.

* Mon Jun 06 2011 Jon Ciesla <limb@jcomserv.net> 2.14.0-1
- Update to 2.14.0.

* Tue May 31 2011 Jon Ciesla <limb@jcomserv.net> 2.13.63-1
- Update to 2.13.63.

* Fri May 27 2011 Jon Ciesla <limb@jcomserv.net> 2.13.62-1
- Update to 2.13.62.

* Mon May 02 2011 Jon Ciesla <limb@jcomserv.net> 2.13.61-1
- Update to 2.13.61.

* Mon Apr 18 2011 Jon Ciesla <limb@jcomserv.net> 2.13.60-1
- Update to 2.13.60.

* Mon Apr 11 2011 Jon Ciesla <limb@jcomserv.net> 2.13.59-1
- Update to 2.13.59.

* Thu Apr 07 2011 Jon Ciesla <limb@jcomserv.net> 2.13.58-1
- Update to 2.13.58.

* Mon Apr 04 2011 Jon Ciesla <limb@jcomserv.net> 2.13.57-1
- Update to 2.13.57.

* Thu Mar 31 2011 Jon Ciesla <limb@jcomserv.net> 2.13.56-1
- Update to 2.13.56.

* Fri Mar 25 2011 Jon Ciesla <limb@jcomserv.net> 2.13.55-1
- Update to 2.13.55.

* Mon Mar 14 2011 Jon Ciesla <limb@jcomserv.net> 2.13.54-1
- Update to 2.13.54.

* Fri Mar 11 2011 Jon Ciesla <limb@jcomserv.net> 2.13.53-2
- Fixed license tag, BZ 684215.

* Tue Mar 08 2011 Jon Ciesla <limb@jcomserv.net> 2.13.53-1
- Update to 2.13.53.

* Wed Mar 02 2011 Jon Ciesla <limb@jcomserv.net> 2.13.52-1
- Update to 2.13.52.

* Fri Feb 25 2011 Jon Ciesla <limb@jcomserv.net> 2.13.51-1
- Update to 2.13.51.

* Mon Feb 14 2011 Jon Ciesla <limb@jcomserv.net> 2.13.50-1
- Update to 2.13.50.

* Thu Feb 10 2011 Jon Ciesla <limb@jcomserv.net> 2.13.49-1
- Update to 2.13.49.

* Tue Feb 08 2011 Jon Ciesla <limb@jcomserv.net> 2.13.48-1
- Update to 2.13.48.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Jon Ciesla <limb@jcomserv.net> 2.13.47-1
- Update to 2.13.47.

* Wed Jan 12 2011 Jon Ciesla <limb@jcomserv.net> 2.13.46-1
- Update to 2.13.46.

* Fri Jan 07 2011 Jon Ciesla <limb@jcomserv.net> 2.13.45-1
- Update to 2.13.45.

* Tue Dec 14 2010 Jon Ciesla <limb@jcomserv.net> 2.13.39-1
- Updat to 2.13.39.

* Mon Jan 04 2010 Jon Ciesla <limb@jcomserv.net> 2.12.3-1
- Update to 2.12.3.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Jon Ciesla <limb@jcomserv.net> 2.12.2-1
- Update to 2.12.2.

* Tue Jan 06 2009 Jon Ciesla <limb@jcomserv.net> 2.12.1-1
- Update to 2.12.1.

* Mon Dec 29 2008 Jon Ciesla <limb@jcomserv.net> 2.12.0-1
- Update to 2.12.0.

* Wed Dec 17 2008 Jon Ciesla <limb@jcomserv.net> 2.11.65-1
- Update to 2.11.65.

* Mon Sep 08 2008 Jon Ciesla <limb@jcomserv.net> 2.11.57-1
- Update to 2.11.57.

* Thu Jan  3 2008 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.33-1
- Update to 2.10.33.
- Compilation fails if the install section doesn't create $RPM_BUILD_ROOT.
- Fix the license tag (GPLv2).
- Misc changes to clean up rpmlint warnings.

* Fri Jan 26 2007 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.13-1
- New release. Fixes bug 224545.

* Wed Dec 20 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.3-1
- New release.

* Thu Nov 16 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.10.0-1
- New release.

* Tue Oct 10 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.7-1
- New release.

* Thu Aug 10 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.6-1
- New release.

* Tue Jun  6 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.4-1
- New release.

* Fri May 19 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.8.3-1
- Initial build.
