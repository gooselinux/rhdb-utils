# Spec file for rhdb-utils.
# Authors: Liam Stewart <liams@redhat.com>, Andrew Overholt
# <overholt@redhat.com>, Tom Lane <tgl@redhat.com>
# Copyright (C) 2002-2010 Red Hat, Inc.

Summary: Miscellaneous utilities for PostgreSQL - Red Hat Edition
Name: rhdb-utils
Version: 8.4.0
Release: 3%{?dist}
URL: http://sources.redhat.com/rhdb/
# pg_crc.c is copied from postgresql, hence MIT; the rest is GPL
License: GPLv2+ and MIT
Group: Applications/Databases

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: postgresql-devel >= 8.4

Source0: http://sources.redhat.com/rhdb/tools/pg_filedump-%{version}.tar
# We keep a copy of pg_crc.c in this SRPM so we don't need to have the
# full PostgreSQL sources to build.  This should be refreshed periodically
# from the PostgreSQL sources.
Source1: pg_crc.c
Patch1: pg_filedump-make.patch

%description
This package contains miscellaneous, non-graphical tools developed for
PostgreSQL - Red Hat Edition.

%prep
%setup -q -n pg_filedump-%{version}

cp %{SOURCE1} pg_crc.c

%patch1 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fwrapv"

make

%install
rm -rf ${RPM_BUILD_ROOT}

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 pg_filedump ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/pg_filedump
%doc ChangeLog README.pg_filedump

%changelog
* Fri Jun  4 2010 Tom Lane <tgl@redhat.com> 8.4.0-3
- Add -fno-strict-aliasing to CFLAGS per rpmdiff complaint, and -fwrapv
  too just to be on the safe side.
Resolves: #596204

* Tue Jan 19 2010 Tom Lane <tgl@redhat.com> 8.4.0-2
- Correct License: tag to reflect that pg_crc.c is copied from postgresql.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 8.4.0-1.1
- Rebuilt for RHEL 6

* Tue Aug 18 2009 Tom Lane <tgl@redhat.com> 8.4.0-1
- Update pg_filedump to version 8.4.0, to support PostgreSQL 8.4.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom Lane <tgl@redhat.com> 8.3.0-1
- Update pg_filedump to version 8.3.0, to support PostgreSQL 8.3.

* Thu Aug  2 2007 Tom Lane <tgl@redhat.com> 8.2.0-2
- Update License tag to match code.

* Wed Feb 14 2007 Tom Lane <tgl@redhat.com> 8.2.0-1
- Update pg_filedump to version 8.2.0, to support PostgreSQL 8.2.
Resolves: #224175

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 8.1.1-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 8.1.1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 8.1.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 21 2005 Tom Lane <tgl@redhat.com> 8.1.1-1
- Update pg_filedump to version 8.1.1, to fix a couple of oversights.
- Simplify specfile a bit.

* Mon Nov 21 2005 Tom Lane <tgl@redhat.com> 8.1-1
- Update pg_filedump to version 8.1, to support PostgreSQL 8.1.
- Change version numbering so that major version matches corresponding
  PostgreSQL version.

* Wed Mar  2 2005 Tom Lane <tgl@redhat.com> 4.0-3
- Rebuild for gcc4 update.

* Fri Feb 11 2005 Tom Lane <tgl@redhat.com> 4.0-2
- Adjust build to honor $RPM_OPT_FLAGS.

* Thu Feb 10 2005 Tom Lane <tgl@redhat.com> 4.0-1
- Update pg_filedump to version 4.0, to support PostgreSQL 8.0.
- Keep pg_crc.c on hand as a plain source file instead of a patch.
  Easier to compare to main PG sources that way.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr  5 2004 Tom Lane <tgl@redhat.com>
- Update outdated URL.

* Fri Feb 20 2004 Tom Lane <tgl@redhat.com>
- Remove beta label from pg_filedump.

* Fri Feb 20 2004 Tom Lane <tgl@redhat.com>
- Update to version 3.0.
- Increment Buildrequires to >= PostgreSQL 7.4
- Rebuild for Fedora Core 2.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Nov 21 2003 David Jee <djee@redhat.com> 2.0-2
- Remove Distribution tag.
- Rebuild for Fedora Core 1.

* Thu May 29 2003 Andrew Overholt <overholt@redhat.com>
- Bump to version 2.0.
- Modify distribution.
- Increment Buildrequires to >= PostgreSQL 7.3

* Wed Sep 11 2002 Andrew Overholt <overholt@redhat.com>
- Changed revision to 1.

* Fri Jul  8 2002 Liam Stewart <liams@redhat.com>
- Updated summary and description.

* Thu Jul  4 2002 Liam Stewart <liams@redhat.com>
- Updated Source0 entry.

* Wed Jun 26 2002 Liam Stewart <liams@redhat.com>
- Group fix.

* Mon Jun 24 2002 Liam Stewart <liams@redhat.com>
- Initial build.


