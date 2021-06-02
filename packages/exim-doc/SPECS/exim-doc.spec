Summary: Documentation for the exim mail transfer agent
Name: exim-doc
Version: 4.73
Release: 15%{?dist}
License: GPLv2
Url: http://www.exim.org/
Source1: ftp://ftp.exim.org/pub/exim/exim4/FAQ-html-20050415.tar.bz2
Source2: ftp://ftp.exim.org/pub/exim/exim4/exim-html-%{version}.tar.bz2
Source3: ftp://ftp.exim.org/pub/exim/exim4/exim-postscript-%{version}.tar.bz2
Source4: ftp://ftp.exim.org/pub/exim/exim4/exim-pdf-%{version}.tar.bz2
Source6: http://www.exim.org/pub/exim/exim4/config.samples-20050415.tar.bz2
BuildArch: noarch

%description
Exim is a mail transport agent (MTA) developed at the University of
Cambridge for use on Unix systems connected to the Internet. This
package contains the documentation for Exim, also available on the 
web at http://www.exim.org/

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%setup -q -T -D -a 1
mv FAQ-html faq
%setup -q -T -D -a 2
mkdir html
mv exim-html-*/doc/html html/doc
%setup -q -T -D -a 3
mv exim-postscript-*/ ps
%setup -q -T -D -a 4
mv exim-pdf-*/ pdf
%setup -q -T -D -a 6

find . -name CVS -type d | xargs rm -rf 

%files
%doc faq html ps pdf config.samples

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.73-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.73-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.73-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.73-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.73-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.73-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.73-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.73-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 David Woodhouse <dwmw2@infradead.org> 4.73-1
- Update to 4.73

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 22 2008 Jon Stanley <jonstanley@gmail.com> - 4.69-2
- Fix license tag

* Thu Jan  3 2008 David Woodhouse <dwmw2@infradead.org> 4.69-1
- Update to 4.69

* Fri Aug 31 2007 David Woodhouse <dwmw2@infradead.org> 4.68-1
- Update to 4.68

* Wed Jul  4 2007 David Woodhouse <dwmw2@redhat.com> 4.67-1
- Update to 4.67

* Tue Feb  6 2007 David Woodhouse <dwmw2@redhat.com> 4.66-1
- Update to 4.66

* Sun Sep  3 2006 David Woodhouse <dwmw2@redhat.com> 4.63-2
- Merge twoerner's 4.62-3.el5 changes into Extras package

* Sun Sep  3 2006 David Woodhouse <dwmw2@redhat.com> 4.63-1
- Update to 4.63

* Mon Jul 17 2006 Thomas Woerner <twoerner@redhat.com> 4.62-3.el5
- fixed buildroot for package review
- dropped CVS from config.samples
- fixed permissions of spec and tar files

* Tue May  2 2006 David Woodhouse <dwmw2@redhat.com> 4.62-2
- Bump release to work around the fact that 'make tag' _still_ doesn't
  make sure that the common directory is up to date, just like it didn't
  half an hour ago.

* Tue May  2 2006 David Woodhouse <dwmw2@redhat.com> 4.62-1
- Update to 4.62

* Tue Apr  4 2006 David Woodhouse <dwmw2@redhat.com> 4.61-1
- Update to 4.61

* Tue Nov 29 2005 David Woodhouse <dwmw2@redhat.com> 4.60-1
- Update to 4.60

* Tue Feb 22 2005 David Woodhouse <dwmw2@redhat.com> 4.50-1
- Move exim-doc into a separate package
